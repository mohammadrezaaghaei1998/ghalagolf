from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AcademyApplicationForm
from . models import GolfAcademyContent,GolfAcademyGallery,GolfAcademyGalleryDescription

def golf_academy(request):
    content = GolfAcademyContent.objects.first()
    gallery = GolfAcademyGallery.objects.all()
    gallery_description = GolfAcademyGalleryDescription.objects.first()
    first_image = gallery.first().image_main.url if gallery.first() and gallery.first().image_main else '{% static "images/default_image.jpg" %}'

    if request.method == 'POST':
        form = AcademyApplicationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print("Saved application:", instance) 
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('golf-academy')
        else:
            print(form.errors) 
            messages.error(request, "There was an error in your submission.")

    else:
        form = AcademyApplicationForm()
    
    return render(request, 'golf_academy.html', {'form': form ,'content': content ,'gallery':gallery, 'first_image': first_image, 'gallery_description':gallery_description})
