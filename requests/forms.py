# requests/forms.py
from django import forms
from .models import CustomerRequest

class CustomerRequestForm(forms.ModelForm):
    class Meta:
        model = CustomerRequest
        fields = ['name', 'email', 'company', 'phone', 'service_type', 'description', 'budget', 'timeline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Company (Optional)'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number (Optional)'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your project needs...', 'rows': 5}),
            'budget': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Budget (Optional)'}),
            'timeline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expected Timeline (Optional)'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(CustomerRequestForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = field in ['name', 'email', 'service_type', 'description']