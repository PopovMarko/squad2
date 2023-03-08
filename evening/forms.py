from django import forms
from .models import *


class SoldierAddForm (forms.ModelForm):

    class Meta:
        model = Soldiers
        fields = '__all__'


class WeaponsUpdateForm (forms.ModelForm):

    class Meta:
        model = Weapons
        fields = '__all__'
