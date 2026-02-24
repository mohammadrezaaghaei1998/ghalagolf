from django.contrib import admin
from .models import MembershipHeader,Amenity,AmenityCategory,GolfFee

# Register your models here.


admin.site.register(MembershipHeader)
admin.site.register(GolfFee)



class AmenityInline(admin.TabularInline):
    model = Amenity
    extra = 1

@admin.register(AmenityCategory)
class AmenityCategoryAdmin(admin.ModelAdmin):
    inlines = [AmenityInline]

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']