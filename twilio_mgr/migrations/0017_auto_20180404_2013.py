# Generated by Django 2.0.3 on 2018-04-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twilio_mgr', '0016_remove_location_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='notes',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
