from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Add product'

    def handle(self, *args, **kwargs):
        client = Client.objects.all()[6]
        product_2 = Product.objects.all()[1]
        order = Order(order_client=client, order_price=5607480)
        order.save()
        order.order_product.set([product_2])
        order.save()
        self.stdout.write(f'{type(order)}')
        self.stdout.write(f'{order.order_client}')
        self.stdout.write(f'{product_2}')
        self.stdout.write(f'{order.order_product}')
        self.stdout.write(f'{Order.objects.all()[3].order_product}')
        self.stdout.write(f'{order.order_product.all()}')

