
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@permission_classes([IsAuthenticated])
class BookingView(APIView):

    def get(self, request):
        return Response({"message": "This view is protected"})

@permission_classes([IsAuthenticated])
class BookingViewSet(ModelViewSet):

    def get(self, request):
        return Response({"message": "This view is protected"})

@permission_classes([IsAuthenticated])
class MenuItemsView(APIView):

    def get(self, request):
        return Response({"message": "This view is protected"})
