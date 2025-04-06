from django.db import models


class RadioFM(models.Model):

    name = models.CharField(max_length=250, verbose_name='Nomnbre de radio')
    img = models.ImageField(upload_to='radio_images', verbose_name='Imagen')
    link = models.URLField(verbose_name='Link de Radio')
    listeners = models.PositiveIntegerField(default=0, verbose_name='Oyentes')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Radio FM'
        verbose_name_plural = 'Radios FM'

        ordering = ['-listeners']
