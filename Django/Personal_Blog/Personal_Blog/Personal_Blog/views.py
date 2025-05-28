from django.shortcuts import HttpResponse, render
from django.urls import path


def redirect_to_home(request):
    return render(request, "home.html")

    
