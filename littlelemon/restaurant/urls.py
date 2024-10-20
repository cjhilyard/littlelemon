
#define URL route for index() view
from django.urls import path
#from .views import BookingView, MenuView
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('', views.index, name='booking'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu' ),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
]