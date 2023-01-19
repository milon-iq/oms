import json

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, Brand, Product, Coupon, Cart, Order, Address
from rest_framework.serializers import SerializerMethodField


class BrandCreateSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class BrandListSerializer(ModelSerializer):
    class Meta:
        model = Brand
        exclude = ["created_at", "updated_at"]


class BrandDetailSerializer(ModelSerializer):
    class Meta:
        model = Brand
        exclude = ['created_at', 'updated_at']


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']


class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']


class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']


class ProductListSerializer(ModelSerializer):
    category = SerializerMethodField()
    brand = SerializerMethodField()

    def get_category(self, instance):
        category_queryset = Category.objects.filter(id=instance.category_id)
        return CategoryDetailSerializer(category_queryset, many=True).data

    def get_brand(self, instance):
        brand_queryset = Brand.objects.filter(id=instance.brand_id)
        return BrandDetailSerializer(brand_queryset, many=True).data

    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']


class ProductDetailSerializer(ModelSerializer):
    category = SerializerMethodField()
    brand = SerializerMethodField()

    def get_category(self, instance):
        category_queryset = Category.objects.filter(id=instance.category_id)
        return CategoryDetailSerializer(category_queryset, many=True).data

    def get_brand(self, instance):
        brand_queryset = Brand.objects.filter(id=instance.brand_id)
        return BrandDetailSerializer(brand_queryset, many=True).data

    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']


class CartDetailSerializer(ModelSerializer):
    class Meta:
        model = Cart
        exclude = ['created_at', 'updated_at']


class CartListSerializer(ModelSerializer):
    product = SerializerMethodField()

    def get_product(self, instance):
        product_queryset = Product.objects.filter(id=instance.product_id)
        return ProductDetailSerializer(product_queryset, many=True).data

    class Meta:
        model = Cart
        exclude = ['created_at', 'updated_at']


class CartCreateAPIView(ModelSerializer):
    class Meta:
        model = Cart
        exclude = ['created_at', 'updated_at']


class CartDetailAPIView(ModelSerializer):
    class Meta:
        model = Cart
        exclude = ['created_at', 'updated_at']


class OrderDetailSerializer(ModelSerializer):
    products = SerializerMethodField()

    def get_products(self, instance):
        return json.loads(instance.products)

    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at']


class OrderListSerializer(ModelSerializer):
    products = SerializerMethodField()

    def get_products(self, instance):
        return json.loads(instance.products)

    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at']


class CouponDetailSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        exclude = ['created_at', 'updated_at']


class CouponListSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        exclude = ['created_at', 'updated_at']


class AddressListSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = ['created_at', 'updated_at']


class AddressRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = ['created_at', 'updated_at']


class AddressCreateSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = ['created_at', 'updated_at']
