from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, Brand, Product, Coupon, Cart, Order


class BrandCreateSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class BrandListSerializer(ModelSerializer):
    class Meta:
        model = Brand
        exclude = ["created_at", "updated_at"]


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']


class CategoryRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']


class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']
