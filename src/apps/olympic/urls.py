from django.urls import path
from .views import home,logout_view,register

urlpatterns = [
    path('',home,name='home-page'),
    path('register/',register,name='register'),
    path('logout/',logout_view,name='logout')
]