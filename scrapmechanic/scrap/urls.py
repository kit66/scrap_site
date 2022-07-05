from django.urls import path
from .views import *

urlpatterns = [

    path('', main, name='mainpage'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser, name='logout'),
    path('profile', profile, name='profile'),
    path('mods', mod.as_view(), name='mods'),
    path('mods/<slug:slug>', about, name='about')
]
