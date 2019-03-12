from django.urls import path, re_path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('', views.login, name='login'),
    path('user_index/', views.user_index, name='user_index'),
    re_path(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    re_path(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    re_path(r'^add_number/(?P<id>\d+)/$', views.add_number, name='add_number'),
    re_path(r'^add_email/(?P<id>\d+)/$', views.add_email, name='add_email'),
    re_path(r'^view/(?P<id>\d+)/$', views.view, name='view'),
    path('add_email/', views.add_email, name='add_email'),
    path('add_number/', views.add_number, name='add_number'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('update_contact/', views.update_contact, name='update_contact'),
    path('logout/', views.logout, name='logout'),

]