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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['emails'] = self.object.to_client.values_list('email', flat=True)

        return context_data


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:list')


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:list')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:list')
