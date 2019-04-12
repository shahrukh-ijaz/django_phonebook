from django.urls import path
from contacts.views import login, sample_api, UserProfile, UserContacts, Logout

urlpatterns = [
    path('api/profile', UserProfile.as_view(), name='profile'),
    path('api/contacts', UserContacts.as_view(), name='contacts'),
    path('api/logout', Logout.as_view(), name='logout'),
    path('api/login', login),
    path('api/sampleapi', sample_api)
]