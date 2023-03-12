from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, UpdateView
from .models import *
from .forms import *


class MaterialIndex(ListView):
    pass
