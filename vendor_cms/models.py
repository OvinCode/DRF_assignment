from typing import Any
from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100,unique=True)
    contact_details = models.TextField()
    address = models.TextField(max_length=200)
    vendor_code = models.AutoField(unique=True,primary_key=True)
    # on_time_delivery_rate = models.FloatField(default=None)
    # quality_rating_avg = models.FloatField(default=None)
    # average_response_time = models.FloatField(default=None)
    # fulfillment_rate = models.FloatField(default=None)

    def __str__(self):
        return self.name


class Order(models.Model):

    ORDER_STATUS_CHOICES = [

        ("pending","PENDING"),
        ("cancelled","CANCELLED"),
        ("delivered","DELIVERED"),
    ]

    po_number = models.AutoField(max_length=10,unique=True,primary_key=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=None)
    status =  models.CharField (max_length=10,choices=ORDER_STATUS_CHOICES)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()
    

    def __str__(self):
        return self.po_number


class Performance(models.Model):

    vendor = models.ForeignKey(Vendor , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=None)
    quality_rating_avg = models.FloatField(default=None)
    average_response_time = models.FloatField(default=None)
    fulfillment_rate = models.FloatField(default=None)


    def __str__(self):
        return self.vendor