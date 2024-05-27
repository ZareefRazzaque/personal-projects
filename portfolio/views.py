from django.shortcuts import render
from portfolio import views


def redirect_home(request):
    return views.home(request)

def home(request):
    return render(request, 'portfolio/templates/home.html')
    