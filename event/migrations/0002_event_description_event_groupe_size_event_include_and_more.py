# Generated by Django 5.1 on 2024-08-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Description',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='event',
            name='Groupe_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='Include',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='event',
            name='Localisation',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Nbr_jours',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Pays',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Programme',
            field=models.TextField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Type',
            field=models.CharField(choices=[('Event', 'Event'), ('Travel Organize', 'Travel Organize'), ('Event of the season', 'Event of the season'), ('Tour Organize', 'Tour Organize'), ('Business event', 'Business Event')], default='', max_length=100),
            preserve_default=False,
        ),
    ]
