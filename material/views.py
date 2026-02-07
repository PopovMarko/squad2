from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib import messages
from django.views.generic import DeleteView, DetailView, ListView, CreateView
from django.views.generic.edit import FormView, UpdateView, FormMixin
from django.views.generic.detail import SingleObjectMixin


from .models import *
from .forms import *


class MaterialList (ListView):
    model = Stock
    template_name = 'material/stock_list.html'


class ConsignmentList (ListView):
    model = Consignment
    template_name = 'material/consignment_list.html'


class ConsignmentGoodsDetail(SingleObjectMixin, FormView):

    model = Consignment
    template_name = 'material/consignment_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Consignment.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Consignment.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return ConsignmentGoodsFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Change were saved'
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('')  # not


class ConsignmentAdd (CreateView):
    model = Consignment
    template_name = 'material/consignment_add.html'
    form_class = ConsignmentAddForm


class ConsignmentUpdate (UpdateView):
    model = ConsignmentGoods
    template_name = 'material/consignment_update.html'
    form_class = ConsignmentGoodsForm


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


class ServiceDetail (DetailView):
    model = Service
    template_name = 'material/service_detail.html'


class ServiceAdd (CreateView):
    model = Service
    template_name = 'material/service_add.html'
    form_class = ServiceAddForm
    success_url = reverse_lazy('service-index')


class ServiceUpdate (UpdateView):
    model = Service
    template_name = 'material/service_update.html'
    form_class = ServiceUpdateForm
    success_url = reverse_lazy('service-index')


class ServiceDelete (DeleteView):
    model = Service
    template_name = 'material/service_delete.html'
    success_url = reverse_lazy('service-index')
