from django.urls import path
from myusers.views import *
urlpatterns = [
    path('login',Login,name='Login'),
    path('logout',Logout,name='Logout'),
    path('registration',Reg,name='Regsitration')
]