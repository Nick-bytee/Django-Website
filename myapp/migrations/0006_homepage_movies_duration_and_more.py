# Generated by Django 4.0.5 on 2022-07-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_homepage_movies_country_homepage_movies_release_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage_movies',
            name='duration',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage_movies',
            name='release_year',
            field=models.IntegerField(),
        ),
    ]
