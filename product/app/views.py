from django.shortcuts import render

# Create your views here.
from app.models import product
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class productlist(ListView):
    model = product


class productView(DetailView):
    model = product

class productCreate(CreateView):
    model = product
    fields = ['Productname', 'Price']
    success_url = reverse_lazy('product_list')


class productUpdate(UpdateView):
    model = product
    fields = ['Productname','Price']
    success_url = reverse_lazy('product_list')

class productDelete(DeleteView):
    model = product
    success_url = reverse_lazy('product_list')