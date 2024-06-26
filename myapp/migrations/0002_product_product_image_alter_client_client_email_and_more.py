# Generated by Django 5.0.4 on 2024-04-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=15, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_telephone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_content',
            field=models.TextField(blank=True),
        ),
    ]
