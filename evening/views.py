# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from . models import *


class SoldiersList(ListView):
    model = Soldiers
    template_name = 'evening/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cont = Soldiers.objects.exclude(surname='').count()
        context['cont'] = cont
        return context


class WeaponsList(ListView):
    model = Weapons
    template_name = 'evening/weapons_list.html'


class SoldiersCard(DetailView):
    model = Soldiers
    template_name = 'evening/soldiers_detail.html'
    context_object_name = 'soldiers_card'


class AmmoList(ListView):
    model = Ammo
    template_name = 'evening/ammo_list.html'
