# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from . models import *
# Create your views here.


class SoldiersList(ListView):
    model = Soldiers
    template_name = 'evening/index.html'


class SoldierCard(DetailView):
    model = Soldiers
    template_name = 'evening/soldier_detaile.html'
    context_object_name = 'soldiers_card'


class WeaponsList(ListView):
    model = Weapons
    template_name = 'evening/weapons_list.html'
