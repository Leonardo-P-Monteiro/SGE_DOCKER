from django.db import models
from category.models import Category
from brands.models import Brand

class Product(models.Model):
    title = models.CharField(max_length=400)
    categroy = models.ForeignKey(Category, on_delete=models.PROTECT,
                related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
            related_name='products')
    description = models.TextField(max_length=10000, blank=True, null=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    