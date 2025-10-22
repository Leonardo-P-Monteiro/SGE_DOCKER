from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Brand)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name',)