from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """Sending an email when an order has been created"""
    order = Order.objects.get(id=order_id)
    subject = f'Order number {order.id}'
    message = f'{order.first_name},\n\nYou have successfully placed an order.\
        Your order id is {order.id}'
    mail_sent = send_mail(subject,
                          message,
                          'admin@podcasts.com',
                          [order.email])
    return mail_sent
