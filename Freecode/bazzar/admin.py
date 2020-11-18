from django.contrib import admin
from .models import Category, DepartmentStore, ShopItem
# Register your models here.

admin.site.register(Category)
admin.site.register(DepartmentStore)
admin.site.register(ShopItem)
# admin.site.register(orderItem)
# admin.site.register(Order)