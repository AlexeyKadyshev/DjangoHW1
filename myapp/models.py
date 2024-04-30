from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=15, verbose_name='Имя')
    client_email = models.EmailField(verbose_name='Электронная почта')
    client_telephone = models.CharField(max_length=20, verbose_name='Телефон')
    client_date_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.client_name}, E-mail: {self.client_email}, Contacts: {self.client_telephone}'


class Product(models.Model):
    product_name = models.CharField(max_length=35, verbose_name='Наименование')
    product_image = models.ImageField(upload_to='product_photos', blank=True, null=True, verbose_name='Изображение')
    product_content = models.TextField(blank=True, verbose_name='Описание')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    product_count = models.IntegerField(verbose_name='Количество')
    product_date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.product_name}, count: {self.product_count}, ' \
               f'price: {self.product_price}, count: {self.product_count}'


class Order(models.Model):
    order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_product = models.ManyToManyField(Product)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Заказ успешно сформирован'
