from django.shortcuts import render
from . models import MembershipHeader,Amenity,AmenitiesSection,AmenityCategory,GolfFee
# Create your views here.


def membership(request):
    membership_header = MembershipHeader.objects.first() 
    section = AmenitiesSection.objects.first()  
    categories = AmenityCategory.objects.prefetch_related('amenities').all()
    golf_fees = GolfFee.objects.all()
    context = {
        'membership_header': membership_header,
        'section': section,
        'categories': categories,
        'golf_fees': golf_fees,
    }
    return render(request, 'membership.html', context)






