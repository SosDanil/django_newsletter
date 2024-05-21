from django.urls import path

from newsletter.apps import NewsletterConfig
from newsletter.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView, NewsletterDeleteView

app_name = NewsletterConfig.name

urlpatterns = [
    path('', NewsletterListView.as_view(), name='list'),
    path('detail/<int:pk>/', NewsletterDetailView.as_view(), name='detail'),
    path('create/', NewsletterCreateView.as_view(), name='create'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete'),
]
