# Generated by Django 4.1.2 on 2022-10-23 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_blogscategories_slug_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DetailsBlog',
        ),
    ]
