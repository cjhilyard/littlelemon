
#define URL route for index() view
from django.urls import path
from .views import BookingView, MenuView

urlpatterns = [
    path('booking/', BookingView.as_view(), name='booking'),
    path('menu/', MenuView.as_view(), name='menu' ),
]