from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from newsletter.forms import NewsletterForm, NewsletterManagerForm
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


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:list')

    login_url = '/users/register/'

    def form_valid(self, form):
        newsletter = form.save()
        user = self.request.user
        newsletter.owner = user
        newsletter.save()
        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:list')

    login_url = '/users/register/'

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsletterForm
        if user.has_perm('newsletter.set_active'):
            return NewsletterManagerForm
        raise PermissionDenied


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:list')

    login_url = '/users/register/'


@login_required(login_url='/users/register/')
def view_try_mailing(request, pk):
    context = {
        'object_list': TryMailing.objects.filter(newsletter=pk),
        'title': 'Попытки рассылки',
    }
    return render(request, 'newsletter/try_mailing.html', context)

