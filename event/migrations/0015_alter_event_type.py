# Generated by Django 5.1 on 2024-09-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_alter_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Type',
            field=models.CharField(choices=[('Travel Organize', 'Travel Organize'), ('Business event', 'Business Event'), ('Tour Organize', 'Tour Organize'), ('Event of the season', 'Event of the season'), ('Event', 'Event')], max_length=100),
        ),
    ]
