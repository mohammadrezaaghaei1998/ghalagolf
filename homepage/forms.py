from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Full Name*'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email Address'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message'
            }),
        }
