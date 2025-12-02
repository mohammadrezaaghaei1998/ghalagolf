from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'id': 'contact-name'}),
            'email': forms.EmailInput(attrs={'id': 'contact-email'}),
            'subject': forms.TextInput(attrs={'id': 'contact-subject'}),
            'message': forms.Textarea(attrs={'id': 'contact-message', 'rows': 3}),
        }










