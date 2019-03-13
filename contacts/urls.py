from django.urls import path, re_path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url( r'^$',auth_views.LoginView.as_view(template_name="contacts/login.html"), name="login"),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # path('', views.index, name=''),
    path('insert/', views.insert, name='insert'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('user_index/', views.user_index, name='user_index'),
    re_path(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    re_path(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    re_path(r'^add_number/(?P<id>\d+)/$', views.add_number, name='add_number'),
    re_path(r'^add_email/(?P<id>\d+)/$', views.add_email, name='add_email'),
    re_path(r'^display_contact/(?P<id>\d+)/$', views.display_contact, name='display_contact'),

    re_path(r'^email_edit/(?P<id>\d+)/(?P<contact_id>\d+)/$', views.email_edit, name='email_edit'),
    re_path(r'^email_delete/(?P<id>\d+)/(?P<contact_id>\d+)/$', views.email_delete, name='email_delete'),
    re_path(r'^number_edit/(?P<id>\d+)/(?P<contact_id>\d+)/$', views.number_edit, name='number_edit'),
    re_path(r'^number_delete/(?P<id>\d+)/(?P<contact_id>\d+)/$', views.number_delete, name='number_delete'),


    path('add_email/', views.add_email, name='add_email'),
    path('add_number/', views.add_number, name='add_number'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('update_contact/', views.update_contact, name='update_contact'),
    # path('logout/', auth_views.logout, name='logout'),

]