from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from .forms import NewForm

# Create your views here.
def home(request):
    return render(request,'app_models/index.html' ,{ 'cars': Car.objects.all()})

def form1(request):
    return render(request, 'app_models/index.html', {'form': NewForm()})
    # return HttpResponse("Django Forms")