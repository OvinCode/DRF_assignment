from django.urls import path
from . import views


urlpatterns=[
    # path('', views.ApiOverview ,name="api_overview"),
    path("", views.CreateVendor,name='create_vendor'),
    path("all", views.GetAllVendor,name='get_all_vendor'),
    path("<int:vendor_id>", views.GetVendor,name='get_vendor'),
    path("update/<int:vendor_id>", views.UpdateVendor,name='update_vendor'),
    path("delete/<int:vendor_id>", views.DeleteVendor,name='delete_vendor'),

]