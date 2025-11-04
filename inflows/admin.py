from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier','product', 'created_at', 'updated_at', \
                    'quantity',)
    search_fields = ('supplier__name','product__title', 'created_at', 'updated_at', \
                    'quantity',)