
from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    """ docstring
    """
    class Meta:
        model = Booking
        fields = '__all__'