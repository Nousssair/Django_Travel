# Generated by Django 5.1 on 2024-08-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Public_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='Type',
            field=models.CharField(choices=[('Event', 'Event'), ('Tour Organize', 'Tour Organize'), ('Business event', 'Business Event'), ('Event of the season', 'Event of the season'), ('Travel Organize', 'Travel Organize')], max_length=100),
        ),
    ]
