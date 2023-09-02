from django.contrib import admin
from .models import Article, Publisher, Review


# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'email', 'phone', 'category', 'item')
#     search_fields = ('full_name', 'email', )
#     list_filter = ('category', )


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('category', 'date_created')
    search_fields = ('category', )
    list_filter = ('category', )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'staff', 'date_created')


# admin.site.register(Article, ArticleAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Review, ReviewAdmin)

