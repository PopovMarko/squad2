from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormView, UpdateView
from django.forms import inlineformset_factory
from .models import *
from .forms import *


class MaterialList (ListView):
    model = Stock
    template_name = 'material/stock_list.html'


class GoodsList (ListView):
    model = Goods
    template_name = 'material/goods_list.html'


class GoodsAdd (CreateView):
    model = Goods
    template_name = 'material/goods_add.html'
    form_class = GoodsAddForm
    success_url = '/index/material/'  # Hardcoded URL must be changed


class ServiceList (ListView):
    model = Service
    template_name = 'material/service_list.html'


class ServiceAdd (CreateView):
    model = Service
    template_name = 'material/service_add.html'
    form_class = ServiceAddForm


class ConsignmentList (ListView):
    model = Consignment
    template_name = 'material/consignment_list.html'


class ConsignmentDetail (DetailView):
    model = Consignment
    template_name = 'material/consignment_detail.html'


class ConsignmentAdd (CreateView):
    model = Consignment
    template_name = 'material/consignment_add.html'
    form_class = ConsignmentAddForm
