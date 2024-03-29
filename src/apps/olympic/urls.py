from django.urls import path
from .views import home,logout_view,register,forgotpassword

urlpatterns = [
    path('',home,name='home-page'),
    path('register/',register,name='register'),
    path('forgot/password/',forgotpassword,name='forgot-password'),
    path('logout/',logout_view,name='logout')
]