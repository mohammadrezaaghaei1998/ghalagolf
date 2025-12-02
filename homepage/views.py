from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HomePageHeader, Service,AboutUs,TeamMember,Insight,ContactMessage, ContactInfo
from .forms import ContactForm
from news .models import News 





def index(request):
    header = HomePageHeader.objects.first()
    services = Service.objects.all().order_by('order')
    about_us = AboutUs.objects.first()
    team_members = TeamMember.objects.all()
    insights = Insight.objects.all()
    latest_news = News.objects.order_by('-publish_date')[:3]
    contact_info = ContactInfo.objects.first()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("index")
        else:
            messages.error(request, "Please fill out all fields correctly.")

    context = {
        "header": header,
        "services": services,
        "about_us": about_us,
        "team_members": team_members,
        "insights": insights,
        "latest_news": latest_news,
        "contact_info": contact_info,
    }
    return render(request, "index.html", context)