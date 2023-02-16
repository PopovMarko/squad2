# from django.shortcuts import render
from django.views.generic import ListView
from ./models import *
# Create your views here.


class SoldiersList(ListView):
    model = models.Soldiers
    template_name = 'soldiers_list.html'
