
from django.urls import path
from . import views
from .views import BrandCreateAPIView, BrandRetrieveAPIView, BrandListAPIView, BrandUpdateAPIView, CategoryListAPIView, \
    CategoryRetrieveAPIView, CategoryCreateAPIView, CategoryUpdateAPIView, ProductListAPIView, ProductCreateAPIView, \
    ProductRetrieveAPIView, ProductUpdateAPIView, CartListAPIView, CartCreateAPIView, CartRetrieveAPIView, \
    CartUpdateAPIView
urlpatterns = [
    path('brand/create/', BrandCreateAPIView.as_view(), name='brand_create'),
    path('brand/detail/<int:pk>/', BrandRetrieveAPIView.as_view(), name='brand_details'),
    path('brand/list/all/', BrandListAPIView.as_view(), name='all_brands_list'),
    path('brand/update/<int:pk>/', BrandUpdateAPIView.as_view(), name='update_brand'),

    path('category/list/all/', CategoryListAPIView.as_view(), name='all_category'),
    path('category/detail/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category_update'),

    path('product/list/all/', ProductListAPIView.as_view(), name='product_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/detail/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_details'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update_product'),

    path('cart/list/all/', CartListAPIView.as_view(), name='cart_list'),
    path('cart/create/', CartCreateAPIView.as_view(), name='cart_create'),
    path('cart/detail/<int:pk>/', CartRetrieveAPIView.as_view(), name='cart_detail'),
    path('cart/update/<int:pk>/', CartUpdateAPIView.as_view(), name='update_cart'),

]
