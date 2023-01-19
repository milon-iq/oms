import json

from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from .models import Brand, Category, Product, Cart, Coupon, Order
from .serializers import BrandCreateSerializer, BrandListSerializer, CategoryListSerializer, CategoryDetailSerializer, \
    CategoryCreateSerializer, ProductCreateSerializer, ProductListSerializer, ProductDetailSerializer, \
    CartDetailSerializer, CartListSerializer, OrderDetailSerializer, OrderListSerializer, CouponListSerializer, \
    CouponDetailSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.


class BrandCreateAPIView(CreateAPIView):
    serializer_class = BrandCreateSerializer
    queryset = Brand.objects.all()
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(tags=['Brand'])
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
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(tags=['Brand'])
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        brand_obj = Brand.objects.filter(pk=pk).first()
        serializer = BrandListSerializer(brand_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class BrandListAPIView(ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(tags=['Brand'])
    def get(self, request, *args, **kwargs):
        queryset = Brand.objects.all()
        serializer = BrandListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class BrandUpdateAPIView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()

    @swagger_auto_schema(tags=['Brand'])
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        # brand_queryset = Brand.objects.filter(pk=pk).update(**request.data)
        brand_queryset = Brand.objects.filter(pk=pk)
        brand_obj = brand_queryset.update(**request.data)
        return Response(data={'details': 'Brand name updated'})


class CategoryListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    @swagger_auto_schema(tags=['Category'])
    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategoryListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()

    @swagger_auto_schema(tags=['Category'])
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        category_obj = Category.objects.filter(pk=pk).first()
        serializer = CategoryDetailSerializer(category_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()

    @swagger_auto_schema(tags=['Category'])
    def post(self, request, *args, **kwargs):
        category_title = request.data.get('category_title', None)
        category_obj = Category(category_title=category_title)
        category_obj.save()
        serializer = CategoryDetailSerializer(category_obj)
        # return Response(data={'details': 'New Category Added'}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CategoryUpdateAPIView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()

    @swagger_auto_schema(tags=['Category'])
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        category_qs = Category.objects.filter(pk=pk).update(**request.data)
        return Response(data={'details': 'Category name Updated'}, status=status.HTTP_200_OK)


class ProductListAPIView(ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

    @swagger_auto_schema(tags=['Product'])
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()

    @swagger_auto_schema(tags=['Product'])
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
        serializer = ProductDetailSerializer(product_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProductRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

    @swagger_auto_schema(tags=['Product'])
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        product_obj = Product.objects.filter(pk=pk).first()
        serializer = ProductDetailSerializer(product_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductUpdateAPIView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

    @swagger_auto_schema(tags=['Product'])
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        product_qs = Product.objects.filter(pk=pk).update(**request.data)
        # serializer = ProductListSerializer(product_qs)
        # return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'details': 'Product detail updated'}, status=status.HTTP_200_OK)


class CartListAPIView(ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CartListSerializer
    queryset = Cart.objects.all()

    @swagger_auto_schema(tags=['Cart'])
    def get(self, request, *args, **kwargs):
        queryset = Cart.objects.all()
        serializer = CartListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CartCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()

    @swagger_auto_schema(tags=['Cart'])
    def post(self, request, *ags, **kwargs):
        data = request.data
        user = User.objects.first()
        for item in data:
            product_id = item['product']
            quantity = item['product_quantity']
            cart_obj = Cart(user=user, product_id=product_id, product_quantity=quantity)
            cart_obj.save()

        return Response(data={'data': 'Products added to cart. '}, status=status.HTTP_201_CREATED)


#
# class CartCreateAPIView(CreateAPIView):
#     serializer_class = CartDetailSerializer
#     queryset = Cart.objects.all()
#
# @swagger_auto_schema(tags=['Cart'])
#     def post(self, request, *ags, **kwargs):
#         data = request.data
#         user = User.objects.first()
#         product = data.get('product', None)
#         product_quantity = data.get('product_quantity', None)
#         # product_queryset = Product.objects.filter(id=product)
#         # product_obj = product_queryset.first()
#         # unit_price = product_obj.product_price
#         cart_obj = Cart(user=user, product_id=product, product_quantity=product_quantity)
#         cart_obj.save()
#         serializer = CartDetailSerializer(cart_obj)
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CartRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()

    @swagger_auto_schema(tags=['Cart'])
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        cart_obj = Cart.objects.filter(pk=pk).first()
        serializer = CartDetailSerializer(cart_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CartUpdateAPIView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()

    @swagger_auto_schema(tags=['Cart'])
    def put(self, request, *args, **kwargs):
        data = request.data
        pk = kwargs.get('pk', None)
        cart_qs = Cart.objects.filter(pk=pk).update(**data)
        return Response(data={'details': 'Cart details updated'}, status=status.HTTP_200_OK)


class OrderListAPIView(ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

    # permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(tags=['Order'])
    def get(self, request, *args, **kwargs):
        queryset = Order.objects.all()

        serializer = OrderListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()

    @swagger_auto_schema(tags=['Order'])
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        order_obj = Order.objects.filter(pk=pk).first()
        if order_obj is None:
            return Response(data={'details': 'No Order found regarding this ID. '}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderDetailSerializer(order_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()

    @swagger_auto_schema(tags=['Order'])
    def post(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.first()
        total_price = 0
        total_quantity = 0
        list_of_product = []
        for item in data["product"]:
            product_id = item["product_id"]
            product_name = item["product_name"]
            quantity = item["quantity"]
            unit_price = item["unit_price"]
            total_quantity += quantity
            total_price += quantity * unit_price
            sample_dict = {
                "product_id": product_id,
                "product_name": product_name,
                "quantity": product_name,
                "unit_price": unit_price
            }
            list_of_product.append(sample_dict)
        products_json = json.dumps(list_of_product)
        final_quantity = total_quantity
        final_price = total_price
        order_obj = Order(user=user, total_quantity=final_quantity, total_price=final_price, products=products_json)
        order_obj.save()
        return Response(data={'details': 'order created'}, status=status.HTTP_201_CREATED)


class OrderUpdateAPIView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()

    @swagger_auto_schema(tags=['Order'])
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        order_qs = Order.objects.filter(pk=pk).update(**request.data)
        return Response(data={'details': 'Order details updated'}, status=status.HTTP_200_OK)


class CouponListAPIView(ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CouponListSerializer
    queryset = Coupon.objects.all()

    @swagger_auto_schema(tags=['Coupon'])
    def get(self, request, *args, **kwargs):
        queryset = Coupon.objects.all()
        serializer = CouponListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CouponRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CouponDetailSerializer
    queryset = Coupon.objects.all()

    @swagger_auto_schema(tags=['Coupon'])
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        coupon_obj = Coupon.objects.filter(pk=pk).first()
        serializer = CouponDetailSerializer(coupon_obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CouponCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CouponDetailSerializer
    queryset = Coupon.objects.all()

    @swagger_auto_schema(tags=['Coupon'])
    def post(self, request, *args, **kwargs):
        data = request.data
        coupon_code = data.get('coupon_code', None)
        discount_amount = data.get('discount_amount', None)
        discount_type = data.get('discount_type', None)
        coupon_start_date = data.get('coupon_start_date', None)
        coupon_end_date = data.get('coupon_end_date', None)

        coupon_obj = Coupon(coupon_code=coupon_code, discount_amount=discount_amount, discount_type=discount_type,
                            coupon_start_date=coupon_start_date, coupon_end_date=coupon_end_date)
        coupon_obj.save()
        serializer = CouponDetailSerializer(coupon_obj)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CouponUpdateAPIView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CouponDetailSerializer
    queryset = Coupon.objects.all()

    @swagger_auto_schema(tags=['Coupon'])
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        coupon_qs = Coupon.objects.filter(pk=pk).update(**request.data)
        return Response(data={'details': 'Coupon details updated'}, status=status.HTTP_200_OK)
