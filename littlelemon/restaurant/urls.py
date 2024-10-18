
#define URL route for index() view
from django.urls import path
from .views import BookingView, MenuView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('booking/', BookingView.as_view(), name='booking'),
    path('menu/', MenuView.as_view(), name='menu' ),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
]