from django.core.management.base import BaseCommand
from myapp.models import Client

name = input('Введите имя клиента: ')
email = input('Введите E-mail клиента: ')
telephone = input('Введите контактный номер клиента: ')


class Command(BaseCommand):
    help = 'Add client'

    def handle(self, *args, **kwargs):
        client = Client(client_name=name, client_email=email,
                        client_telephone=telephone)
        client.save()
        self.stdout.write(f'{client}')
