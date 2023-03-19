from django import forms
from django.forms import inlineformset_factory

from .models import *


class ConsignmentAddForm (forms.ModelForm):
    class Meta:
        model = Consignment
        fields = '__all__'


class ServiceAddForm (forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class GoodsAddForm (forms.ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'


# class ConsignmentWithGoodsForm()
