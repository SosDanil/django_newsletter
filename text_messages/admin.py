from django.contrib import admin

from text_messages.models import TextMessage


@admin.register(TextMessage)
class TextMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body',)
    search_fields = ('subject', 'body',)
