# Generated by Django 4.1.2 on 2022-10-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TracksMusicArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracks_images', models.ImageField(upload_to='tracks_images/', verbose_name='')),
                ('tracks_title', models.CharField(max_length=150, verbose_name='')),
                ('tracks_date_added', models.DateField(verbose_name='')),
                ('tracks_music', models.FileField(upload_to='tracks_music/', verbose_name='')),
            ],
            options={
                'verbose_name': 'Треки Музыкальной Зоны',
                'verbose_name_plural': 'Треки Музыкальной Зоны',
            },
        ),
    ]