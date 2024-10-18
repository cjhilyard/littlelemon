
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingView(APIView):

    def get(self, request):
        pass

class BookingViewSet(ModelViewSet):

    def get(self, request):
        pass

class MenuView(APIView):

    def get(self, request):
        pass
