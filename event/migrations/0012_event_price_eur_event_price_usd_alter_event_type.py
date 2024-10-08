# Generated by Django 5.1 on 2024-09-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_category_event_date_alter_event_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price_eur',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='price_usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='Type',
            field=models.CharField(choices=[('Event of the season', 'Event of the season'), ('Event', 'Event'), ('Tour Organize', 'Tour Organize'), ('Business event', 'Business Event'), ('Travel Organize', 'Travel Organize')], max_length=100),
        ),
    ]
