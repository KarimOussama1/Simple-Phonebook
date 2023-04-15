from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Contact, Phone
from .serializers import ContactSerializer

def index(request):
    return render(request, 'index.html')

def show_contacts(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'show_contacts.html', context)

def contact_detail(request, id):
    try:
        contact = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        raise Http404("Contact does not exist")
    print("\t\t\tContact: ", contact.phone_numbers.all())
    context = {'contact': contact}
    return render(request, 'contact_detail.html', context)

def new_contact(request):
    return render(request, 'new_contact.html')

def add_contact(request):
    name = request.POST['contact_name']
    try:
        contact = Contact(name=name)
        contact.save()
    except:
        raise Http404("Name is invalid")
    
    for field in request.POST:
        if field.startswith('phone_number'):
            phone = Phone(number=request.POST[field], contact=contact)
            phone.save()

    print(request.POST)
    return redirect('phonebook:show_contacts')
