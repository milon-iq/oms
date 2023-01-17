from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Brand, Category, Product, Cart, Coupon, Order
from .serializers import BrandCreateSerializer, BrandListSerializer, CategoryListSerializer, CategoryRetrieveSerializer, \
    CategoryCreateSerializer, ProductCreateSerializer, ProductListSerializer, CartDetailSerializer, CartListSerializer
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


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        product_code = data.get('product_code', None)
        product_name = data.get('product_name', None)
        brand = data.get('brand', None)
        category = data.get('category', None)
        product_price = data.get('product_price', None)
        stock_in = data.get('stock_in', None)
        stock_out = data.get('stock_out', None)
        product_availability = data.get('product_availability', None)
        product_description = data.get('product_description', None)

        product_obj = Product(product_code=product_code, product_name=product_name, brand_id=brand,
                              category_id=category,
                              product_price=product_price, stock_in=stock_in, stock_out=stock_out,
                              product_availability=product_availability, product_description=product_description)
        product_obj.save()
        serializer = ProductListSerializer(product_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        product_obj = Product.objects.filter(pk=pk).first()
        serializer = ProductListSerializer(product_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        product_qs = Product.objects.filter(pk=pk).update(**request.data)
        # serializer = ProductListSerializer(product_qs)
        # return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'details': 'Product detail updated'}, status=status.HTTP_200_OK)


class CartListAPIView(ListAPIView):
    serializer_class = CartListSerializer
    queryset = Cart.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Cart.objects.all()
        serializer = CartListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CartCreateAPIView(CreateAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()

    def post(self, request, *ags, **kwargs):
        data = request.data
        user_id = data.get('user_id', None)
        product_id = data.get('product_id', None)
        product_quantity = data.get('product_quantity', None)
        cart_obj = Cart(user_id_id=user_id, product_id_id=product_id, product_quantity=product_quantity)
        cart_obj.save()
        serializer = CartDetailSerializer(cart_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CartRetrieveAPIView(RetrieveAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()

    def get(self, request, *args, **kwargs):
        pk=kwargs.get('pk', None)
        cart_obj = Cart.objects.filter(pk=pk).first()
        serializer = CartDetailSerializer(cart_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CartUpdateAPIView(UpdateAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()

    def put(self, request, *args, **kwargs):
        data = request.data
        pk=kwargs.get('pk', None)
        cart_qs = Cart.objects.filter(pk=pk).update(**data)
        return Response(data={'details': 'Cart details updated'}, status=status.HTTP_200_OK)