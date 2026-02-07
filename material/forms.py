from django import forms
from django.forms import inlineformset_factory

from .models import *


class ConsignmentAddForm (forms.ModelForm):
    class Meta:
        model = Consignment
        fields = ('cons_number', 'cons_date', 'cons_agent', 'cons_status')
        widgets = {
            'cons_number': forms.TextInput(attrs={'class': "form-control-sm"}),
            'cons_date': forms.TextInput(attrs={'class': "form-control-sm"}),
            'cons_agent': forms.Select(attrs={'class': "form-control-sm"}),
            'cons_status': forms.CheckboxInput(attrs={'class': "form-control-sm"}),
        }


class ConsignmentGoodsForm (forms.ModelForm):
    class Meta:
        model = ConsignmentGoods
        fields = ['goods_ref', 'quantity']


ConsignmentGoodsFormSet = inlineformset_factory(
    Consignment, ConsignmentGoods, fields=('goods_ref', 'quantity',), extra=1)


class ServiceAddForm (forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceUpdateForm (forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class GoodsAddForm (forms.ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'
