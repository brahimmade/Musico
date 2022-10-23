# Generated by Django 4.1.2 on 2022-10-23 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_instagramfeeds_alter_recentpost_recent_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cat', to='blog.blogscategories', verbose_name='Категория поста'),
        ),
        migrations.AlterField(
            model_name='blogposts',
            name='blog_title',
            field=models.CharField(max_length=150, unique=True, verbose_name='Заголовок'),
        ),
    ]
