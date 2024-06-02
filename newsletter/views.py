from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter, TryMailing


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


def view_try_mailing(request, pk):
    # breed_item = Breed.objects.get(pk=pk)
    context = {
        'object_list': TryMailing.objects.filter(newsletter=pk),
        'title': 'Попытки рассылки',
    }
    return render(request, 'newsletter/try_mailing.html', context)

# class TryMailingView(ListView):
#     model = TryMailing
#     extra_context = {
#         'title': 'Попытки рассылки'
#     }
#
#     # def get_context_data(self, **kwargs):
#     #     context_data = super().get_context_data(**kwargs)
#     #
#     #     return context_data
#     #
#     def get_queryset(self, *args, **kwargs):
#         queryset = super().get_queryset()
#         queryset = TryMailing.objects.filter(newsletter=)
#         return queryset
