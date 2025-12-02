from django.contrib import admin
from .models import HomePageHeader,Service,AboutUs,TeamMember,Insight,ContactMessage,ContactInfo

# Register your models here.


@admin.register(HomePageHeader)
class HomePageHeaderAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")





@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("order", "title")
    list_editable = ("order",)
    list_display_links = ("title",) 



@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_title', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    search_fields = ('author_name', 'author_title', 'quote')



admin.site.register(AboutUs)
admin.site.register(TeamMember)
admin.site.register(ContactMessage)
admin.site.register(ContactInfo)