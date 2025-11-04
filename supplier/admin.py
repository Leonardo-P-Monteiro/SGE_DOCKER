from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Supllier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ('name', 'created_at', 'updated_at',)