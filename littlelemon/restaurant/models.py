
from django.db import models
from django.db.models import IntegerField, DateField


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    no_of_guests = models.IntegerField()
    bookingdate = DateField()

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    #inventory = Inventory()
