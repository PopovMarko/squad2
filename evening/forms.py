from django import forms
from .models import *


class SoldierAddForm (forms.ModelForm):

    class Meta:
        model = Soldiers
        fields = '__all__'
        widgets = {
            'rank': forms.Select(attrs={'class': 'form-control'}),
        }
