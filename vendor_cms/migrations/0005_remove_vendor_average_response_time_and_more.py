# Generated by Django 5.0.4 on 2024-04-30 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_cms', '0004_alter_vendor_average_response_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='average_response_time',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='fulfillment_rate',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='on_time_delivery_rate',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='quality_rating_avg',
        ),
    ]