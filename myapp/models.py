from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=15)
    client_email = models.EmailField()
    client_telephone = models.CharField(max_length=20)
    client_date_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.client_name}, E-mail: {self.client_email}, Contacts: {self.client_telephone}'


class Product(models.Model):
    product_name = models.CharField(max_length=35)
    product_content = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_count = models.IntegerField()
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
        return f'Заказ успешно сформирован.'
