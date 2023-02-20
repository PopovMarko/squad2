# from django.shortcuts import render
from django.views.generic import ListView
from . models import *
# Create your views here.


class SoldiersList(ListView):
    model = Soldiers
    template_name = 'evening/index.html'
