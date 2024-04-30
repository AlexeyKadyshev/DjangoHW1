import logging

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import date, timedelta

from .forms import AddClientForm, AddProductsForm, ImageForm
from .models import Client, Product, Order

logger = logging.getLogger(__name__)

menu_index = [{'title': 'О сайте', 'url_name': 'website'},
              {'title': 'Каталог', 'url_name': 'catalog'},
              {'title': 'Контакты', 'url_name': 'contacts'},
              {'title': 'Информация о заказах', 'url_name': 'about'},
              {'title': 'Регистрация', 'url_name': 'registration'},
              {'title': 'Добавить товар в каталог', 'url_name': 'add_products'}]

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

    clients = Client.objects.filter(client_date_registration__gte=sort_period).order_by('client_name')
    data = {'clients': clients, 'period': ru}
    return render(request, 'myapp/client_sort.html', context=data)


def registration(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddClientForm()
        print('Error')

    data = {'form': form}
    return render(request, 'myapp/registration.html', data)


def add_products(request):
    if request.method == 'POST':
        form = AddProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('index')
    else:
        form = AddProductsForm()
    data = {'form': form}
    return render(request, 'myapp/add_products.html', data)


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    data = {'form': form}
    return render(request, 'myapp/upload_image.html', data)
