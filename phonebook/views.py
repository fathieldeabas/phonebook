from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView
from .models import Contact, User
from .forms import ContactForm,UserForm

class ContactListView(ListView):
    model = Contact
    template_name = 'phonebook/contact_list.html'

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'phonebook/contact_form.html'
    success_url = '/'

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'phonebook/contact_detail.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'phonebook/contact_form.html'
    success_url = '/'