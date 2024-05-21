from django.urls import path

from text_messages.apps import TextMessagesConfig
from text_messages.views import TextMessageListView, TextMessageDetailView, TextMessageCreateView, TextMessageUpdateView, TextMessageDeleteView

app_name = TextMessagesConfig.name

# Пустые кавычки - идем от корня
urlpatterns = [
    path('', TextMessageListView.as_view(), name='list'),
    path('detail/<int:pk>/', TextMessageDetailView.as_view(), name='detail'),
    path('create/', TextMessageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TextMessageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TextMessageDeleteView.as_view(), name='delete'),
]
