from django.contrib import admin
from .models import AcademyApplication,GolfAcademyContent,GolfAcademyGallery,GolfAcademyGalleryDescription

admin.site.register(GolfAcademyContent)
admin.site.register(GolfAcademyGallery)
admin.site.register(GolfAcademyGalleryDescription)

@admin.register(AcademyApplication)
class AcademyApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'membership_type', 'submitted_at')
    list_filter = ('membership_type', 'submitted_at')
    search_fields = ('full_name', 'email', 'phone')



