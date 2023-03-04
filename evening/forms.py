from django import forms
from .models import *


class SoldierAddForm (forms.ModelForm):
    class Meta:
        model = Soldiers
        fields = '__all__'
