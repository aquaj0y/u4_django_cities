# Generated by Django 4.2.11 on 2024-03-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_rename_city_attraction_citie'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='review',
            name='review_title',
            field=models.TextField(default=''),
        ),
    ]
