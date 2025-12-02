from django import forms
from .models import PartnershipApplication

class PartnershipApplicationForm(forms.ModelForm):
    class Meta:
        model = PartnershipApplication
        fields = [
            'full_name',
            'company_name',
            'cr_number',
            'email',
            'phone',
            'additional_notes',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'cr_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': ' '}),
        }
        labels = {
            'full_name': 'Full Name',
            'company_name': 'Company Name',
            'cr_number': 'CR No (Registration Number)',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'additional_notes': 'Additional Notes',
        }
