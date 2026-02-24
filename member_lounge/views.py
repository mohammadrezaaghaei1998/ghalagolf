from django.shortcuts import render
from .models import MemberLoungeHeader,MemberLoungeDescription,LoungeFeature,MemberLoungeGallery,LoungeBannerInfo

def member_lounge(request):
    header = MemberLoungeHeader.objects.first()
    member_lounge_description = MemberLoungeDescription.objects.first()
    features = LoungeFeature.objects.all()
    gallery_images = MemberLoungeGallery.objects.all()[:6]
    banner_info = LoungeBannerInfo.objects.first()

    context = {
        "header": header,
        "member_lounge_description": member_lounge_description,
        "features": features,
        "gallery_images": gallery_images,
        "banner_info": banner_info,
    }
    return render(request, "member-lounge.html", context)









