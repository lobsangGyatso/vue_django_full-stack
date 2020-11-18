from django.contrib import admin
from .models import Product,orderItem,Order,Category
# Register your models here.

admin.site.register(Product)
admin.site.register(orderItem)
admin.site.register(Order)
admin.site.register(Category)