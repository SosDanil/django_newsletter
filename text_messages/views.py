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


class TextMessageCreateView(CreateView):
    model = TextMessage
    form_class = TextMessageForm
    success_url = reverse_lazy('messages:list')


class TextMessageUpdateView(UpdateView):
    model = TextMessage
    form_class = TextMessageForm
    success_url = reverse_lazy('messages:list')


class TextMessageDeleteView(DeleteView):
    model = TextMessage
    success_url = reverse_lazy('messages:list')

