from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from .models import *
from .forms import *


class StaffList(ListView):
    model = Staff
    template_name = "evening/staff_list.html"


class StaffDetail(DetailView):
    model = Soldiers
    template_name = "evening/staff_detail.html"
    context_object_name = "staff_detail"


class SoldiersList(ListView):
    model = Soldiers
    template_name = "evening/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cont = Soldiers.objects.exclude(surname="").count()
        context["cont"] = cont
        return context


class StaffUpdate(UpdateView):
    model = Soldiers
    template_name = "evening/staff_update.html"
    form_class = StaffUpdateForm


class WeaponsList(ListView):
    model = Weapons
    template_name = "evening/weapons_list.html"


class WeaponsDetaile(UpdateView):
    model = Weapons
    template_name = "evening/weapons_update.html"
    form_class = WeaponsUpdateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.get_object()
        return kwargs


class WeaponsAdd (CreateView):
    model = Weapons
    template_name = 'evening/weapons_add.html'
    form_class = WeaponsAddForm


class AmmoList(ListView):
    model = Ammo
    template_name = "evening/ammo_list.html"
