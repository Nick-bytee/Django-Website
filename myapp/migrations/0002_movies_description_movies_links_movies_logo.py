# Generated by Django 4.0.5 on 2022-06-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='links',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='logo',
            field=models.ImageField(default=0, upload_to='images'),
            preserve_default=False,
        ),
    ]