from django import forms
from .models import *


class StaffUpdateForm (forms.ModelForm):

    class Meta:
        model = Soldiers
        fields = (
            'surname', 'name', 'fathers_name', 'callsign',
            'rank', 'phone', 'birth_date', 'passport', 'tax_number', 'blood_type',
            'addres', 'complect_center', 'mob_date', 'children', 'hight_s', 'size',
            'boots_s', 'head_s', 'photo',
        )

        widgets = {
            'surname': forms.TextInput(attrs={'class': "form-control-sm"}),
            'name': forms.TextInput(attrs={'class': "form-control-sm"}),
            'fathers_name': forms.TextInput(attrs={'class': "form-control-sm"}),
            'callsign': forms.TextInput(attrs={'class': "form-control-sm"}),
            'rank': forms.Select(attrs={'class': "form-control-sm"}),
            'phone': forms.TextInput(attrs={'class': "form-control-sm"}),
            'birth_date': forms.TextInput(attrs={'class': "form-control-sm"}),
            'passport': forms.TextInput(attrs={'class': "form-control-sm"}),
            'tax_number': forms.TextInput(attrs={'class': "form-control-sm"}),
            'blood_type': forms.TextInput(attrs={'class': "form-control-sm"}),
            'addres': forms.TextInput(attrs={'class': "form-control-sm"}),
            'complect_center': forms.TextInput(attrs={'class': "form-control-sm"}),
            'mob_date': forms.TextInput(attrs={'class': "form-control-sm"}),
            'children': forms.TextInput(attrs={'class': "form-control-sm"}),
            'hight_s': forms.TextInput(attrs={'class': "form-control-sm"}),
            'size': forms.TextInput(attrs={'class': "form-control-sm"}),
            'boots_s': forms.TextInput(attrs={'class': "form-control-sm"}),
            'head_s': forms.TextInput(attrs={'class': "form-control-sm"}),
            'photo': forms.FileInput(attrs={'class': "form-control-sm"}),

        }


class WeaponsUpdateForm (forms.ModelForm):

    class Meta:
        model = Weapons
        fields = (
            'weapon_name', 'weapon_number', 'weapon_type', 'weapon_registration',
            'year_manufacture', 'soldier_ref'
        )

        widgets = {
            'weapon_name': forms.TextInput(attrs={'class': "form-control-sm"}),
            'weapon_number': forms.TextInput(attrs={'class': "form-control-sm"}),
            'weapon_type': forms.Select(attrs={'class': "form-control-sm"}),
            'weapon_registration': forms.TextInput(attrs={'class': "form-control-sm"}),
            'year_manufacture': forms.TextInput(attrs={'class': "form-control-sm"}),
            'soldier_ref': forms.Select(attrs={'class': "form-control-sm"}),
        }


class WeaponsAddForm (forms.ModelForm):

    class Meta:
        model = Weapons
        fields = (
            'weapon_name', 'weapon_number', 'weapon_type', 'weapon_registration',
            'year_manufacture', 'soldier_ref'
        )
