from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow
from whatassistent.client import CallMeBot
from datetime import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            # Aqui reside um desafio de lógica. Pois caso o número a ser 
            # subtraido seja maior que o estoque, deveria levantar um erro.
            product.quantity -= instance.quantity
            product.save()

@receiver(post_save, sender=Outflow)
def send_outflow_event(sender, instance:Outflow, created, **kwargs):
    try:
        if created:
            notification = CallMeBot()
            date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            product_name = instance.product.title
            quantity = instance.quantity
            sales_value = instance.product.selling_price
            sales_profit = instance.product.selling_price - instance.product.cost_price
            description = instance.description

            # BUILDING THE MESSAGE TO WHATSAPP ALERT
            outflow_message = f'''
▶️ *SAÍDA REALIZADA NO SGE*

🗓️Data: *{date}*
📦Produto: *{product_name}*
🧮Quantidade: *{quantity}*
💲Valor da venda: *R$ {sales_value}*
💲Lucro com a venda: *R$ {sales_profit}*
📋Descrição: {description}
'''
            # SENDING THE WHATSAPP NOTIFICATION

            notification.send_message(outflow_message)

            # SENDING THE E-MAIL
            send_mail(
            subject='Nova Saída SGE',
            message='Teste',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_ADMIN_RECEIVER],
            html_message=render_to_string(
                template_name='email.html',
                context={
                    'product': product_name,
                    'quantity': quantity,
                    'total_value': sales_value,
                    'profit_value': sales_profit,
                }
            ),
            fail_silently=False, 
            )


    except Exception as e:
        print('ERRO: Ocorreu um erro no signal do envio de mensagem para' \
        f'o whatsapp e email do model outflow. Erro: {type(e).__name__}: {e}')