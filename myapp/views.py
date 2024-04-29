import logging
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import date, timedelta

from .models import Client, Product, Order

logger = logging.getLogger(__name__)

menu_index = [{'title': 'О сайте', 'url_name': 'website'},
              {'title': 'Каталог', 'url_name': 'catalog'},
              {'title': 'Контакты', 'url_name': 'contacts'},
              {'title': 'Информация о заказах', 'url_name': 'about'}]

menu_orders = [{'title': 'Товары', 'url_name': 'products'},
               {'title': 'Клиенты', 'url_name': 'clients'},
               {'title': 'Заказы', 'url_name': 'orders'}, ]


# Create your views here.
def index(request):
    logger.info('Index page accessed')
    data = {
        'menu': menu_index,
        'title': 'Главная страница сайта'
    }
    return render(request, 'myapp/index.html', context=data)


def website(request):
    logger.info('Website page accessed')
    return render(request, 'myapp/website.html')


def contacts(request):
    logger.info('Contacts page accessed')
    return render(request, 'myapp/contacts.html')


def catalog(request):
    logger.info('Catalog page accessed')
    return render(request, 'myapp/catalog.html')


def about(request):
    logger.info('About page accessed')
    data = {
        'menu': menu_orders,
        'title': 'Информация о заказах'
    }
    return render(request, 'myapp/about.html', context=data)


# Заказы
def show_orders(request):
    logger.info('Orders page accessed')
    orders = Order.objects.all()
    data = {'orders': orders}
    return render(request, 'myapp/orders.html', data)


# Товары
def show_products(request):
    logger.info('Products page accessed')
    products = Product.objects.all()
    data = {'products': products}
    return render(request, 'myapp/products.html', data)


# Клиенты
def show_clients(request):
    logger.info('Clients page accessed')
    clients = Client.objects.all()
    data = {'clients': clients}
    return render(request, 'myapp/clients.html', data)


# Информация о товарах клиента за указанный период
def show_client_product(request, client_id, period):
    date_now = date.today()
    client = get_object_or_404(Client, pk=client_id)
    if period == 'day':
        sort_period = date_now - timedelta(days=1)
        ru = 'день'
    elif period == 'week':
        sort_period = date_now - timedelta(days=7)
        ru = 'неделю'
    elif period == 'month':
        sort_period = date_now - timedelta(days=30)
        ru = 'месяц'
    elif period == 'year':
        sort_period = date_now - timedelta(days=365)
        ru = 'год'
    else:
        return render(request, 'myapp/error.html')

    orders = Order.objects.filter(order_client=client, order_date_add__gte=sort_period).order_by('order_date_add')
    products = []
    for order in orders:
        products.extend(order.order_product.all())

    products = set(products)
    data = {'products': products, 'period': ru, 'client': client}
    return render(request, 'myapp/client.html', context=data)


# Все клиенты за указанный период
def client_sort(request, period):
    date_now = date.today()
    match period:
        case ('day'):
            sort_period = date_now - timedelta(days=1)
            ru = 'день'
        case ('week'):
            sort_period = date_now - timedelta(days=7)
            ru = 'неделю'
        case ('month'):
            sort_period = date_now - timedelta(days=30)
            ru = 'месяц'
        case ('year'):
            sort_period = date_now - timedelta(days=365)
            ru = 'год'
        case _:
            return render(request, 'myapp/error.html')

    clients = Client.objects.filter(client_date_registration__gte=sort_period).order_by('client_name')
    data = {'clients': clients, 'period': ru}
    return render(request, 'myapp/client_sort.html', context=data)
