from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            # Aqui reside um desafio de lógica. Pois caso o número a ser 
            # subtraido seja maior que o estoque, deveria levantar um erro.
            product.quantity -= instance.quantity
            product.save()