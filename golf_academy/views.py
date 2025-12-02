from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AcademyApplicationForm

def golf_academy(request):
    if request.method == 'POST':
        form = AcademyApplicationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print("Saved application:", instance)  # For debugging
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('golf-academy')
        else:
            print(form.errors)  # To see validation errors if any
            messages.error(request, "There was an error in your submission.")

    else:
        form = AcademyApplicationForm()
    
    return render(request, 'golf_academy.html', {'form': form})
