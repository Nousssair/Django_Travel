# Generated by Django 5.1 on 2024-09-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_rename_price_eur_event_price_remove_event_price_usd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Type',
            field=models.CharField(choices=[('Business event', 'Business Event'), ('Tour Organize', 'Tour Organize'), ('Event of the season', 'Event of the season'), ('Travel Organize', 'Travel Organize'), ('Event', 'Event')], max_length=100),
        ),
    ]
