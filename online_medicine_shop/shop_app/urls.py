
from django.urls import path
from . import views
from .views import BrandCreateAPIView, BrandRetrieveAPIView, BrandListAPIView, BrandUpdateAPIView
urlpatterns = [
    path('brand/create/', BrandCreateAPIView.as_view(), name='brand_create'),
    path('brand/detail/<int:pk>/', BrandRetrieveAPIView.as_view(), name='brand_details'),
    path('brand/list/all/', BrandListAPIView.as_view(), name='all_brands_list'),
    path('brand/update/<int:pk>/', BrandUpdateAPIView.as_view(), name='update_brand'),


]
