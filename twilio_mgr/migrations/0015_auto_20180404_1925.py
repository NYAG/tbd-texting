# Generated by Django 2.0.3 on 2018-04-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twilio_mgr', '0014_location_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
