from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_created',
        'is_published',
    )

    class Media:
        js = ('js/tinyInject.js',)
