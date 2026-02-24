from django.contrib import admin
from .models import NewsHeader, News

# Register your models here.


admin.site.register(NewsHeader)



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publish_date')
    list_filter = ('category', 'publish_date')
    search_fields = ('title', 'author', 'content')
    ordering = ('-publish_date',)
