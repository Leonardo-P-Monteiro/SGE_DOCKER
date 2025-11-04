from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'brand', 'cost_price', \
                    'selling_price', 'quantity',)
    search_fields = ('title','category__name', 'brand__name', 'cost_price', \
                    'selling_price', 'quantity',)