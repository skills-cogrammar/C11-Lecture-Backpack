# sport_app/views.py

from django.shortcuts import render, redirect
from .models import Registration
from . import forms
from django.contrib.auth.decorators import permission_required


# Create your views here.
def index(request):     # For each page that DOES NOT need authentication
    return render(request, 'sport_app/index.html')


def registrants(request):
    """
    Renders the page displaying all registered users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template for registrants or redirect to login page if not authenticated.
    """
    if request.user and request.user.is_authenticated:
        # Retrieve all registered users
        registrants = Registration.objects.all()
        return render(request, 'sport_app/registrants.html',
                      context={'registrants': registrants, 'user': request.user})
    return redirect('login')


@permission_required('sport_app.add_registration', login_url='registrants')
def sport_registration(request):
    """
    Handles sport registration.

    If the user is authenticated, processes the registration form.
    Redirects to the registrants page upon successful registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template for sport registration or redirect to login page if not authenticated.
    """
    if request.user and request.user.is_authenticated:
        if request.method == 'POST':
            registration_form = forms.SportRegisterForm(request.POST)
            if registration_form.is_valid():
                # Create a new registration entry
                new_registration = Registration.objects.create(
                    user = request.user,
                    sport = registration_form.cleaned_data['sport'],
                    team_name = registration_form.cleaned_data['team_name']
                )
                new_registration.save()
                return redirect('registrants')
        form = forms.SportRegisterForm()
        return render(request, 'sport_app/registration.html', context={'form': form})
    return redirect('login')


def delete_registration(request, id):
    """
    Deletes a registration entry.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the registration entry to delete.

    Returns:
        HttpResponse: Redirect to the registrants page.
    """
    registration = Registration.objects.get(pk=id)
    registration.delete()
    return redirect('registrants')
