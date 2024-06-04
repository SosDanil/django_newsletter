from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'body', 'publish_date', 'counts_of_view')
    ordering = ('publish_date',)
    search_fields = ('title', 'body',)
