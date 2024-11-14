from django import forms
from .models import Client

class clientform(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # Using all fields from the Client model

        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px; width: 100%; margin: 10px auto;',  # Increased width and centered
                'placeholder': 'Full Name'
            }),
            'Clicode': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px; width: 100%; margin: 10px auto;',  # Increased width and centered
                'placeholder': 'Client Code'
            }),
            'position': forms.Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px; width: 100%; margin: 10px auto;',  # Increased width and centered
            }),
            'case_no': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px; width: 100%; margin: 10px auto;',  # Increased width and centered
            }),
            'other_parties': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px; width: 100%; margin: 10px auto;',  # Increased width and centered
                'placeholder': 'Other Parties'
            }),
            'other_partiesreps': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px; width: 100%; margin: 10px auto;',  # Increased width and centered
                'placeholder': 'Other Parties Representatives'
            }),
        }
