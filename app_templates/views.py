from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'app_templates/home.html')

def about(request):
    return render(request,'app_templates/about.html')

def contact(request):
    return render(request,'app_templates/contact.html')
