from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormView, UpdateView
from django.forms import inlineformset_factory
from .models import *
from .forms import *


class MaterialList (ListView):
    model = Stock
    template_name = 'material/stock_list.html'


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


ConsignmentGoodsFormSet = inlineformset_factory(
    Consignment, ConsignmentGoods, form=ConsignmentGoodsForm, extra=2)


class ConsignmentGoodsUpdate (UpdateView):
    model = Consignment
    template_name = 'material/consignment_goods_list.html'
    fields = '__all__'
    success_url = '/'
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ConsignmentGoodsFormSet(
                self.request.POST, instance=self.object)
        else:
            data['formset'] = ConsignmentGoodsFormSet(instance=self.object)
        return data

        # class ConsignmentGoodsList (FormView):
        #     form_class = ConsignmentGoodsFormSet
        #     template_name = 'material/consignment_goods_list.html'
        #     success_url = '/'
        #
        #     def get_queryset(self):
        #         queryset = ConsignmentGoods.objects.filter(
        #             consignment_ref_id=self.kwargs['pk'])
        #         return queryset


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
