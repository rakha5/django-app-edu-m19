from django import forms
from django.core import validators
from .models import Order
from django.contrib.auth.models import Group


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(min_value=1, max_value=100000, decimal_places=2)
#     description = forms.CharField(
#         label='Product description',
#         widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}),
#         # validators=[validators.RegexValidator(
#         #     regex=r'great',
#         #     message='Field must contain word "great"'
#         # )]
#     )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'delivery_address', 'promocode', 'user', 'products'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = 'name',
