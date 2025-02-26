# sport_app/forms.py

from django import forms
from .models import Registration


class SportRegisterForm(forms.ModelForm):
    """
    Form for sport registration.
    """
    class Meta:
        """
        Meta class specifying the model and fields for the form.

        Attributes:
            model (Registration): Model associated with the form.
            fields (list): Fields to include in the form.
        """
        model = Registration
        # Model associated with the form.
        fields = ['sport', 'team_name']
        # Fields to include in the form.
