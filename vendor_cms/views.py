from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# from django.contrib import 
from . models import Vendor,Order,Performance
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import VendorSerializer

@api_view(['GET'])
def ApiOverview(request):
    api_urls={
        'message':"Hi welcome to API"
    }
    return Response(api_urls)

@api_view(['POST'])
def CreateVendor(request):

    Serializer = VendorSerializer(data=request.data)
    if Serializer.is_valid():
        Serializer.save()


    return Response(Serializer.data)


@api_view(['GET'])
def GetAllVendor(request):

    vendor_list = list(Vendor.objects.all().values())
    return Response({"vendors":vendor_list,"message":'All Vendors Returned'},status=200)


@api_view(['GET'])
def GetVendor(request,vendor_id):

    vendor = Vendor.objects.get(vendor_code=vendor_id)
    Serializer = VendorSerializer(instance=vendor, many=False)
    return Response(Serializer.data, status=200)


@api_view(['PUT'])
def UpdateVendor(request,vendor_id):

    vendor = Vendor.objects.get(vendor_code=vendor_id)
    Serializer = VendorSerializer(instance=vendor, data=request.data)
    if Serializer.is_valid():
        Serializer.save()

    return Response(Serializer.data)


@api_view(['DELETE'])
def DeleteVendor(request,vendor_id):

    vendor = Vendor.objects.get(vendor_code=vendor_id)
    vendor.delete()
    
    return JsonResponse({"message":' Vendor Deleted Successfully'},status=200)

