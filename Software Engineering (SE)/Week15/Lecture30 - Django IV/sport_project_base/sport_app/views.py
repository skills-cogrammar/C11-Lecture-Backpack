# sport_app/views.py

from django.shortcuts import render, redirect


# Create your views here.
def index(request):     # For each page that DOES NOT need authentication
    return render(request, 'sport_app/index.html')


def protected_view(request):   # For each page that DOES need authentication
    return render(request, 'sport_app/protected.html')
