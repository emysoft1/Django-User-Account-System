from django import forms
from .models import Department

class ContactForm(forms.Form):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select Department",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}),
        max_length=200
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
