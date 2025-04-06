# Generated by Django 5.1.5 on 2025-02-03 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RadioFM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nomnbre de radio')),
                ('img', models.ImageField(upload_to='radio_images', verbose_name='Imagen')),
                ('link', models.URLField(verbose_name='Link de Radio')),
                ('listeners', models.PositiveIntegerField(default=0, verbose_name='Oyentes')),
            ],
            options={
                'verbose_name': 'Radio FM',
                'verbose_name_plural': 'Radios FM',
                'ordering': ['-listeners'],
            },
        ),
    ]
