# flake8: noqa: E402
import os
import django
import time
import schedule
import requests

from concurrent.futures import ThreadPoolExecutor

# 🚀 Configuración para standalone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # ← Ajusta si tu archivo settings tiene otro nombre
django.setup()

from django.db import close_old_connections
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
        return radio_id, None


def radio_fm_get_listeners():
    radios_db = RadioFM.objects.all()
    urls = [(r.id, r.link) for r in radios_db]

    with ThreadPoolExecutor(max_workers=5) as executor:
        listeners_radio = list(executor.map(fetch_data, urls))

    for radio_id, listeners in listeners_radio:
        if listeners is not None:
            RadioFM.objects.filter(id=radio_id).update(listeners=listeners)

    print("Oyentes actualizados:", listeners_radio)
    close_old_connections()


def main():
    radio_fm_get_listeners()
    schedule.every(5).minutes.do(radio_fm_get_listeners)

    print("✅ Script iniciado. Ejecutando cada 5 minutos...")
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
