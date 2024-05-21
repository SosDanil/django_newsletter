from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Клиенты'
    }


class ClientDetailView(DetailView):
    model = Client
    extra_context = {
        'title': 'Информация о клиенте'
    }


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:list')
