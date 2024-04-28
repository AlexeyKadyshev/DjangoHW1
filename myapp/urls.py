from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('website/', views.website, name='website'),
    path('catalog/', views.catalog, name='catalog'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/clients/<int:client_id>/<slug:period>/', views.show_client_product, name='client'),
    path('about/product/', views.show_products, name='products'),
    path('about/orders/', views.show_orders, name='orders'),
    path('about/clients/', views.show_clients, name='clients'),
    path('about/clients/<slug:period>/', views.client_sort, name='client_sort')
]