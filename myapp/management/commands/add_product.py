from django.core.management.base import BaseCommand


from myapp.models import Product

name = input('Введите наименование товара: ')
content = input('введите описание товара: ')
price = input('Введите цену за единицу товара: ')
count = input('Введите количество заказанного товара: ')


class Command(BaseCommand):
    help = 'Add product'

    def handle(self, *args, **kwargs):
        product = Product(product_name=name, product_content=content,
                          product_price=price, product_count=count)
        product.save()
        self.stdout.write(f'{product}')
