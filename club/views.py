
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact,AboutUs
# Create your views here.


def about_us(request):
    timeline_events = AboutUs.objects.all()
    return render(request, 'about-us.html', {'timeline_events': timeline_events})






def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not subject or not message:
            messages.error(request, "All fields are required.")
            return redirect('contact-us')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact-us')

    return render(request, 'contact-us.html')









