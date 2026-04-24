from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request, my_id):
    return render(request, 'profile.html', {'id': my_id})