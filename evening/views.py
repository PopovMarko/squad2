from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from .models import *
from .forms import *


class SoldiersList(ListView):
    model = Soldiers
    template_name = "evening/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cont = Soldiers.objects.exclude(surname="").count()
        context["cont"] = cont
        return context


class SoldiersCard(DetailView):
    model = Soldiers
    template_name = "evening/soldiers_detail.html"
    context_object_name = "soldiers_card"


class SoldierCardRenew(UpdateView):
    model = Soldiers
    template_name = "evening/soldier_renew.html"
    form_class = SoldierAddForm

    # def get_success_url(self):
    #     return reverse("index")

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['instance'] = self.get_object()
    #     return kwargs


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


class StaffList(ListView):
    model = Staff
    template_name = "evening/staff_index.html"


class Test(ListView):
    model = Soldiers
    template_name = "evening/test.html"
