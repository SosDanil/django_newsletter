from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', NewsletterListView.as_view(), name='list'),
    path('detail/<int:pk>/', NewsletterDetailView.as_view(), name='detail'),
    path('create/', NewsletterCreateView.as_view(), name='create'),
]
