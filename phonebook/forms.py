from django import forms
from .models import Contact,User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'number', 'user']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']