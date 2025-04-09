from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


class RadioFM(models.Model):

    name = models.CharField(max_length=250, verbose_name='Nomnbre de radio')
    img = models.ImageField(upload_to='radio_images', verbose_name='Imagen')
    link = models.URLField(verbose_name='Link de Radio')
    listeners = models.PositiveIntegerField(default=0, verbose_name='Oyentes')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Verifica que exista imagen y que aún no se haya optimizado (evita reconversión)
        if self.img and not self.img.name.lower().endswith('_opt.jpg'):
            try:
                # Abrir la imagen original
                image = Image.open(self.img)
                # Si la imagen tiene transparencia o no está en formato RGB, convierte a RGB
                if image.mode in ('RGBA', 'P'):
                    image = image.convert('RGB')
                # (Opcional) Redimensionar la imagen a un máximo de 300x300 píxeles
                image.thumbnail((300, 300))

                # Guardar la imagen optimizada en memoria en formato JPEG
                buffer = BytesIO()
                image.save(buffer, format='JPEG', optimize=True, quality=75)
                buffer.seek(0)

                # Cambia el nombre de la imagen, añadiendo el sufijo '_opt.jpg'
                new_name = self.img.name.rsplit('.', 1)[0] + '_opt.jpg'
                self.img.save(new_name, ContentFile(buffer.read()), save=False)
            except Exception as e:
                print("Error al optimizar la imagen:", e)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Radio FM'
        verbose_name_plural = 'Radios FM'

        ordering = ['-listeners']
