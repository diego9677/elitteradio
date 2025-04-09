import time
import schedule
import requests

from django.db import close_old_connections
from concurrent.futures import ThreadPoolExecutor

from core.models import RadioFM


def fetch_data(data):
    radio_id, url = data

    try:
        response = requests.get(f'{url}/stats?json=1', timeout=5)
        response.raise_for_status()
        result = response.json()
        current_listeners = int(result.get('currentlisteners', 0))
        return radio_id, current_listeners
    except Exception as e:
        print(f"Error con {url}: {e}")
        return radio_id, 0  # En caso de error, setea oyentes en 0


def radio_fm_get_listeners():
    radios_db = RadioFM.objects.all()
    urls = [(r.id, r.link) for r in radios_db]

    with ThreadPoolExecutor(max_workers=5) as executor:
        listeners_radio = list(executor.map(fetch_data, urls))

    # Actualizar oyentes en la base de datos
    for radio_id, listeners in listeners_radio:
        RadioFM.objects.filter(id=radio_id).update(listeners=listeners)

    print("Oyentes actualizados:", listeners_radio)
    close_old_connections()


def run():

    radio_fm_get_listeners()
    schedule.every(5).minutes.do(radio_fm_get_listeners)

    print("running")
    while True:
        schedule.run_pending()
        time.sleep(1)
