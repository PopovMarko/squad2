from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormView, UpdateView
from django.forms import inlineformset_factory
from .models import *
from .forms import *


class MaterialList (ListView):
    model = Stock
    template_view = 'material/stock_list.html'


class GoodsList (ListView):
    model = Goods
    template_view = 'material/goods_list.html'


class ServiceList (ListView):
    model = Service
    template_view = 'material/service_list.html'


class ConsignmentList (ListView):
    model = Consignment
    template_name = 'material/consignment_list.html'
