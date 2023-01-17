from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Brand, Category, Product
from .serializers import BrandCreateSerializer, BrandListSerializer, CategoryListSerializer, CategoryRetrieveSerializer, \
    CategoryCreateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class BrandCreateAPIView(CreateAPIView):
    serializer_class = BrandCreateSerializer
    queryset = Brand.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        brand_title = data.get('brand_title', None)
        brand_obj = Brand(brand_title=brand_title)
        brand_obj.save()
        serializer = BrandListSerializer(brand_obj)
        return Response(data={'created_data': serializer.data, 'details': 'New Brand Added'},
                        status=status.HTTP_201_CREATED)


class BrandRetrieveAPIView(RetrieveAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        brand_obj = Brand.objects.filter(pk=pk).first()
        serializer = BrandListSerializer(brand_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class BrandListAPIView(ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Brand.objects.all()
        serializer = BrandListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class BrandUpdateAPIView(UpdateAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        brand_queryset = Brand.objects.filter(pk=pk).update(**request.data)
        return Response(data={'details': 'Brand name updated'})


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategoryListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        category_obj = Category.objects.filter(pk=pk).first()
        serializer = CategoryRetrieveSerializer(category_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        category_title = request.data.get('category_title', None)
        category_obj = Category(category_title=category_title)
        category_obj.save()
        serializer = CategoryRetrieveSerializer(category_obj)
        # return Response(data={'details': 'New Category Added'}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CategoryRetrieveSerializer
    queryset = Category.objects.all()

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        category_qs = Category.objects.filter(pk=pk).update(**request.data)
        return Response(data={'details': 'Category name Updated'}, status=status.HTTP_200_OK)