from datetime import datetime

from django.forms import widgets

from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    """ docstring
    """
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'reservation_date': widgets.DateInput(attrs={'type': 'date', 'value': datetime.now().strftime("%d-%m-%Y")}),
        }