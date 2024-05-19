from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter


class NewsletterListView(ListView):
    model = Newsletter
    extra_context = {
        'title': 'Главная'
    }


class NewsletterDetailView(DetailView):
    model = Newsletter
    extra_context = {
        'title': 'Информация о рассылке'
    }


class NewsletterCreateView(CreateView):
    model = Newsletter
    extra_context = {
        'title': 'Создание рассылки'
    }
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:list')
