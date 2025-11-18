from products.models import Product
from outflows.models import Outflow
from django.utils.formats import number_format
from django.db.models import Sum


def get_product_metric():
    products = Product.objects.all()
    total_cost_price = sum(product.quantity * product.cost_price for \
                           product in products)
    total_quantity = sum(p.quantity for p in products)
    total_selling_price = sum(p.selling_price * p.quantity for p in products)
    total_profit = total_selling_price - total_cost_price
    
    product_metrics = {
        'total_quantity': total_quantity,
        'total_cost_price': number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        'total_selling_price': number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        'total_profit':number_format(total_profit, decimal_pos=2, force_grouping=True),
    } 

    return product_metrics

def get_sales_metrics():

    outflow_query= Outflow.objects.all()
    total_sales = Outflow.objects.count()
    total_products_sold = Outflow.objects.aggregate(
        total_products_sold = Sum('quantity')
    )['total_products_sold'] or 0
    total_sales_values = sum(o.product.selling_price * o.quantity for o in outflow_query )
    total_sales_cost = sum(o.product.cost_price * o.quantity for o in outflow_query)
    total_sales_profit = total_sales_values - total_sales_cost


    sales_metrics = {
        'total_sales': total_sales,
        'total_products_sold': number_format(total_products_sold, decimal_pos=2, force_grouping=True),
        'total_sales_values': number_format(total_sales_values, decimal_pos=2, force_grouping=True),
        'total_sales_profit': number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    }

    return sales_metrics