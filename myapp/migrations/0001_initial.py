# Generated by Django 5.0.4 on 2024-04-21 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=15)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_telephone', models.CharField(max_length=20)),
                ('client_date_registration', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=35)),
                ('product_content', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_count', models.IntegerField()),
                ('product_date_add', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date_add', models.DateField(auto_now_add=True)),
                ('order_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
                ('order_product', models.ManyToManyField(to='myapp.product')),
            ],
        ),
    ]