from django import forms
from django.forms import inlineformset_factory

from .models import *


class ConsignmentAddForm (forms.ModelForm):
    class Meta:
        model = Consignment
        fields = '__all__'


class ConsignmentGoodsForm (forms.ModelForm):
    class Meta:
        model = ConsignmentGoods
        fields = '__all__'


# ConsignmentGoodsFormSet = modelformset_factory(
#     Consignment, ConsignmentGoods, form=ConsignmentGoodsForm, mextra=2)


class ServiceAddForm (forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class GoodsAddForm (forms.ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'
