from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Наименование")
    description = forms.CharField(max_length=2000, required=False, label='Описание',widget=widgets.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False, label='Категория')
    amount = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')

