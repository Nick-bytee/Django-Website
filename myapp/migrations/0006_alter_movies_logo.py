# Generated by Django 4.0.5 on 2022-06-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_rating_movies_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='logo',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
