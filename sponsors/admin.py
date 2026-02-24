from django.contrib import admin
from .models import SponsorHeader,PartnershipSection,Partner,PartnershipApplication

# Register your models here.


admin.site.register(SponsorHeader)
admin.site.register(PartnershipSection)
admin.site.register(Partner)


@admin.register(PartnershipApplication)
class PartnershipApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company_name', 'email', 'phone', 'submitted_at')
    readonly_fields = ('submitted_at',)
