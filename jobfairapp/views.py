from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'navbar.html')

def login(request):
    return render(request,'login.html')