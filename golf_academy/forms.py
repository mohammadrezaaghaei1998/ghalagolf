from django import forms
from .models import AcademyApplication

class AcademyApplicationForm(forms.ModelForm):
    class Meta:
        model = AcademyApplication
        fields = [
            'full_name', 'email', 'phone', 'membership_type', 
            'message', 'handicap', 'dob'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'membership_type': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' ', 'rows': 3}),
            'handicap': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': ' ', 'type': 'date'}),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'membership_type': 'Membership Type',
            'message': 'Additional Notes',
            'handicap': 'Golf Handicap (Optional)',
            'dob': 'Date of Birth',
        }
