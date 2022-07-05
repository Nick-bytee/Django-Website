# Generated by Django 4.0.5 on 2022-07-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_homepage_movies_movie_id_homepage_movies_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage_movies',
            name='new',
        ),
        migrations.AddField(
            model_name='homepage_movies',
            name='trailer',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage_movies',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]