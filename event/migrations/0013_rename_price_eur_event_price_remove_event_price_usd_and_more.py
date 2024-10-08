# Generated by Django 5.1 on 2024-09-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_event_price_eur_event_price_usd_alter_event_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='price_eur',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='event',
            name='price_usd',
        ),
        migrations.AddField(
            model_name='event',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='event',
            name='Type',
            field=models.CharField(choices=[('Travel Organize', 'Travel Organize'), ('Event', 'Event'), ('Event of the season', 'Event of the season'), ('Business event', 'Business Event'), ('Tour Organize', 'Tour Organize')], max_length=100),
        ),
    ]
