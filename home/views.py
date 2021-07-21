from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core import serializers
from django import forms
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, "registpage.html")

def dashboard(request):
    return render(request, "dashboard.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        details = Contact.objects.all()
        contact = Contact(name = name, email = email, dob = dob, phone = phone, password = password)
        contact.save()
        messages.success(request, 'You are successfully registered!')
        return render(request, "dashboard.html", {details : details})
    return render(request, "register.html")