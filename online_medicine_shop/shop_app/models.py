from django.db import models
from systems.models import BaseModel
from systems.enums import DiscountType, AddressType
from django.contrib.auth.models import User


# Create your models here.
class Brand(BaseModel):
    brand_title = models.CharField(max_length=50, help_text='brand name')

    class Meta:
        db_table = 'brands'


class Category(BaseModel):
    category_title = models.CharField(max_length=50, help_text='category name')

    class Meta:
        db_table = 'categories'


class Product(BaseModel):
    product_code = models.CharField(max_length=100, help_text='product code')
    product_name = models.CharField(max_length=100, help_text='name of product')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, help_text=' brand name of a product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text=' category of the product')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, help_text='price of product')
    stock_in = models.IntegerField(help_text='product stocked in the shop')
    stock_out = models.IntegerField(null=True, blank=True, help_text='amount of product sell from the shop')
    product_availability = models.IntegerField(help_text='amount of available product')
    product_description = models.TextField(help_text='description of products')

    class Meta:
        db_table = 'products'


class Cart(BaseModel):
    user = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='product id')
    product_quantity = models.IntegerField(help_text='amount of product want to buy')

    class Meta:
        db_table = 'carts'


class Coupon(BaseModel):
    coupon_code = models.CharField(max_length=50, help_text='coupon code')
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='discount amount of a product')
    discount_type = models.CharField(max_length=10, choices=DiscountType.choices(), default=DiscountType.AMOUNT.value)
    coupon_start_date = models.DateTimeField(auto_now_add=False)
    coupon_end_date = models.DateTimeField(auto_now_add=False)

    class Meta:
        db_table = 'coupons'


class Address(BaseModel):
    address = models.CharField(max_length=500, help_text='address of the of user')
    upazila = models.TextField(help_text=' Upazila name of the user')
    district = models.TextField(help_text='District name of the user')
    division = models.TextField(help_text='Division name of the user')
    contact_no = models.IntegerField(help_text='user mobile number')
    address_type = models.CharField(max_length=10, choices=AddressType.choices(), default=AddressType.SHIPPING_ADDRESS.
                                    value)

    class Meta:
        db_table = 'addresses'


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text=' user id')
    total_quantity = models.IntegerField(help_text='amount of products want to order')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, help_text='total prices of products')
    products = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'orders'

