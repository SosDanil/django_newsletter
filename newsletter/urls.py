from django.urls import path
from django.views.decorators.cache import cache_page

from newsletter.apps import NewsletterConfig
from newsletter.views import (NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView,
                              NewsletterDeleteView, view_try_mailing, MainView)

app_name = NewsletterConfig.name

urlpatterns = [
    path('', cache_page(60)(MainView.as_view()), name='main'),
    path('list/', NewsletterListView.as_view(), name='list'),
    path('detail/<int:pk>/', NewsletterDetailView.as_view(), name='detail'),
    path('create/', NewsletterCreateView.as_view(), name='create'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete'),
    path('<int:pk>/try_mailing/', view_try_mailing, name='try_mailing'),
]
