from django.contrib import admin

from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'client_telephone', 'client_date_registration', 'brief_info')
    list_display_links = ('client_name',)
    ordering = ['client_date_registration', 'client_name']
    list_per_page = 5
    search_fields = ['client_name']
    list_filter = ['client_date_registration']

    @admin.display(description='Информация о клиенте')
    def brief_info(self, client: Client):
        return f'Здесь может быть размещена краткая информация о {client.client_name}'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['product_name', 'product_price', 'product_count', 'product_content']
    list_display = (
    'product_name', 'product_content', 'product_price', 'product_count', 'product_date_add', 'brief_info')
    list_display_links = ('product_name',)
    ordering = ['product_date_add', 'product_name']
    list_per_page = 5
    search_fields = ['product_name']
    list_filter = ['product_date_add']

    @admin.display(description='Краткое описание')
    def brief_info(self, product: Product):
        return f'Информация о {product.product_name} {len(product.product_content)} символов'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_client', 'order_price', 'order_date_add')
    list_display_links = ('order_client',)
    ordering = ['order_date_add', 'order_client']
    list_per_page = 5

# admin.site.register(Client, ClientAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Order, OrderAdmin)
