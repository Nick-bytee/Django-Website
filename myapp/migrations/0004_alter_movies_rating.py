# Generated by Django 4.0.5 on 2022-06-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_movies_rating_movies_age_movies_quality_movies_type1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Rating',
            field=models.FloatField(max_length=2),
        ),
    ]