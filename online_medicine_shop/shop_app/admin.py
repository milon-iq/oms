from django.contrib import admin
from .models import Brand, Category, Cart, Coupon, Order, Product,Address


# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(Address)
