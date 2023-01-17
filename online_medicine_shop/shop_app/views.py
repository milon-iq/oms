from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Brand, Category, Product
from .serializers import BrandCreateSerializer, BrandListSerializer
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
        return Response(data={'created_data': serializer.data, 'details': 'New Brand Added'}, status=status.HTTP_201_CREATED)


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


