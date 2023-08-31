from django.contrib import admin
from .models import Article, Publisher


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'category', 'item')
    search_fields = ('full_name', 'email', )
    list_filter = ('category', )


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_created')
    search_fields = ('title', 'category', )
    list_filter = ('category', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Publisher, PublisherAdmin)
