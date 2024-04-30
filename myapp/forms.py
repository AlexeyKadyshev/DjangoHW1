from django import forms
from .models import Client, Product, Order


# class AddClientForm(forms.Form):
#     client_name = forms.CharField(min_length=5, max_length=25, label='Имя')
#     client_email = forms.EmailField(label='Электронная почта')
#     client_telephone = forms.CharField(min_length=5, max_length=12, label='Телефон')


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_email', 'client_telephone']


class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'product_content', 'product_price', 'product_count']
        widgets = {
            'product_content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }


class ImageForm(forms.Form):
    image = forms.ImageField()