# Generated by Django 4.2.16 on 2024-09-13 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0025_alter_event_description_alter_event_localisation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Type',
            field=models.CharField(choices=[('Event of the season', 'Event of the season'), ('Business event', 'Business Event'), ('Tour Organize', 'Tour Organize'), ('Travel Organize', 'Travel Organize'), ('Event', 'Event')], max_length=100),
        ),
    ]
