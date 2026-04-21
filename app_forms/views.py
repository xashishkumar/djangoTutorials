from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm

# Create your views here.

def home(request):
    return render(request, 'app_forms/index.html', {'form': 'ProfileForm'})
    # return HttpResponse("Forms")