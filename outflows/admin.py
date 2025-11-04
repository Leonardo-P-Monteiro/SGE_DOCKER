from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at',)
    search_fields = ('product__title', 'quantity', 'created_at',)