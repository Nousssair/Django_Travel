# Generated by Django 5.1 on 2024-08-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_description_event_groupe_size_event_include_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Type',
            field=models.CharField(choices=[('Event', 'Event'), ('Tour Organize', 'Tour Organize'), ('Travel Organize', 'Travel Organize'), ('Business event', 'Business Event'), ('Event of the season', 'Event of the season')], max_length=100),
        ),
    ]
