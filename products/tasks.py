# products/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from .models import Product

@shared_task
def process_order(order_data):
    # Process the order and update inventory levels
    items = order_data['items']
    for item in items:
        product = Product.objects.get(sku=item['sku'])
        product.quantity -= item['quantity']
        product.save()

    # Send an email to the customer confirming the order
    customer_email = order_data['customer']['email']
    send_mail(
        'Order Confirmation',
        'Thank you for your order!',
        'noreply@example.com',
        [customer_email],
        fail_silently=False,
    )