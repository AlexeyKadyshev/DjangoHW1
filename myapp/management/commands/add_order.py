from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Add product'

    def handle(self, *args, **kwargs):
        for i in range(10):
            client = Client.objects.all()[i]

            product_1 = Product.objects.all()[0]
            product_2 = Product.objects.all()[1]
            product_3 = Product.objects.all()[2]

            order = Order(order_client=client, order_price=5607480)
            order.save()
            order.order_product.set([product_1, product_2, product_3])

            self.stdout.write(f'{order}')
