from django.shortcuts import render, redirect
from .models import SponsorHeader,PartnershipSection,Partner
from django.contrib import messages
from .forms import PartnershipApplicationForm


# Create your views here.

def sponsors(request):
    header = SponsorHeader.objects.first()
    partnership = PartnershipSection.objects.first()
    partners = Partner.objects.all()

    if request.method == "POST":
        form = PartnershipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('sponsors') 
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PartnershipApplicationForm()

    return render(request, 'sponsors.html', {
        'header': header,
        'partnership': partnership,
        'partners': partners,
        'form': form,
    })
