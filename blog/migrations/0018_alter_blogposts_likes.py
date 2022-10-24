# Generated by Django 4.1.2 on 2022-10-24 12:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0017_alter_blogposts_likes_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]