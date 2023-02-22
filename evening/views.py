# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from . models import *
# Create your views here.


class SoldiersList(ListView):
    model = Soldiers
    template_name = 'evening/index.html'


class SoldiersDetaileList(DetailView):
    model = Soldiers
    template_name = 'evening/soldiersdetaile.html'


class WeaponsList(ListView):
    model = Weapons
    template_name = 'evening/weapons_list.html'
