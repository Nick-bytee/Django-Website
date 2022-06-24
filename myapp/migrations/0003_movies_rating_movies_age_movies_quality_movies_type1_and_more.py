# Generated by Django 4.0.5 on 2022-06-24 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_movies_description_movies_links_movies_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='Rating',
            field=models.IntegerField(default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='age',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='quality',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='type1',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='type2',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movies',
            name='logo',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]