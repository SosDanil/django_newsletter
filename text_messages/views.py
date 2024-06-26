from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from text_messages.forms import TextMessageForm
# from text_messages.forms import TextMessageForm
from text_messages.models import TextMessage


class TextMessageListView(ListView):
    model = TextMessage
    extra_context = {
        'title': 'Сообщения'
    }


class TextMessageDetailView(DetailView):
    model = TextMessage
    extra_context = {
        'title': 'Содержание сообщения'
    }


class TextMessageCreateView(LoginRequiredMixin, CreateView):
    model = TextMessage
    form_class = TextMessageForm
    success_url = reverse_lazy('messages:list')

    login_url = '/users/register/'

    def form_valid(self, form):
        text_message = form.save()
        user = self.request.user
        text_message.owner = user
        text_message.save()
        return super().form_valid(form)


class TextMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = TextMessage
    form_class = TextMessageForm
    success_url = reverse_lazy('messages:list')

    login_url = '/users/register/'


class TextMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = TextMessage
    success_url = reverse_lazy('messages:list')

    login_url = '/users/register/'
