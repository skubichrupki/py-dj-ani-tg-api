# Generated by Django 4.2.19 on 2025-02-23 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotes',
            name='quote_text',
        ),
        migrations.AddField(
            model_name='quotes',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 23, 18, 47, 50, 203248, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='quotes',
            name='quote_anime_name',
            field=models.CharField(default=''),
        ),
        migrations.AddField(
            model_name='quotes',
            name='quote_character_name',
            field=models.CharField(default=''),
        ),
        migrations.AddField(
            model_name='quotes',
            name='quote_content',
            field=models.CharField(default=''),
        ),
    ]
