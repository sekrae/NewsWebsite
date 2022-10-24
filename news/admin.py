from django.contrib import admin
from . models import News

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'category',
        'body',
        'feature_image',
        'author',
        'pub_date',
    )
    list_filter = ('pub_date', 'title', 'category', 'author')

    search_fields = ('pub_date', 'title', 'body')
    prepopulated_fields = {'slug':['title']}

