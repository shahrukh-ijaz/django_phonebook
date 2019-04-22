from django.urls import path
from contacts.api import login, UserProfile, UserContacts, Logout

urlpatterns = [
    path('api/profile', UserProfile.as_view(), name='profile'),
    path('api/contacts', UserContacts.as_view(), name='contacts'),
    path('api/logout', Logout.as_view(), name='logout'),
    path('api/login', login)
]
