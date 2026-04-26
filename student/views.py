from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request, my_id):

    messages.success(request, "successfully fetch")
    return render(request, 'profile.html', {'id': my_id})



def register(request):

    return render(request, 'register.html')

def login(request):

    return render(request, 'login.html')

def forgot(request):

    return render(request, 'forgot.html')