from django.urls import path, re_path, include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout

from . import views

urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(template_name="contacts/login.html"), name="login"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('user_index/', views.user_index, name='user_index'),
    re_path(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    re_path(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    re_path(r'^add_number/(?P<id>\d+)/$', views.add_number, name='add_number'),
    re_path(r'^add_email/(?P<id>\d+)/$', views.add_email, name='add_email'),
    re_path(r'^display_contact/(?P<id>\d+)/$', views.display_contact, name='display_contact'),

    re_path(r'^email_delete/(?P<id>\d+)/(?P<contact_id>\d+)/$', views.email_delete, name='email_delete'),
    re_path(r'^number_delete/(?P<id>\d+)/(?P<contact_id>\d+)/$', views.number_delete, name='number_delete'),

    path('logout/', include('django.contrib.auth.urls'), name="logout"),
    path('add_email/', views.add_email, name='add_email'),
    path('create_email/', views.create_email, name='create_email'),
    path('add_number/', views.add_number, name='add_number'),
    path('create_number/', views.create_number, name='create_number'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('update_contact/', views.update_contact, name='update_contact'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]