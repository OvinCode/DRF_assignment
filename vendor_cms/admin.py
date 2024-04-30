from django.contrib import admin
from .models import Order,Vendor,Performance

# Register your models here.

admin.site.register(Order)
admin.site.register(Vendor)
admin.site.register(Performance)
