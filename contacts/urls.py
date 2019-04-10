from collections import UserList

from django.urls import path, re_path, include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from . import views
from contacts.views import UserAPIView, ContactAPIView, ContactDetails, UserDetails, login, sample_api

urlpatterns = [
    # django rest urls below
    re_path('users/$', UserAPIView.as_view(), name='user_list'),
    re_path('contacts/$', ContactAPIView.as_view(), name='contact_list'),
    path('user/<int:pk>', UserDetails.as_view(), name='user_details'),
    path('contact/<int:pk>', ContactDetails.as_view(), name='contact_list'),
    path('api/login', login),
    path('api/sampleapi', sample_api)
]