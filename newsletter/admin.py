from django.contrib import admin

from newsletter.models import Newsletter, TryMailing


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('message', 'status', 'first_mailing', 'last_mailing', 'periodicity')
    list_filter = ('status', 'periodicity', 'message',)
    search_fields = ('message',)


@admin.register(TryMailing)
class TryMailingAdmin(admin.ModelAdmin):
    list_display = ('newsletter', 'status', 'last_try')
    list_filter = ('status',)
    search_fields = ('newsletter',)
