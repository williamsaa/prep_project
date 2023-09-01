from django.conf.urls import include, url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login_user/', views.login_user, name='login_user'),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
 
] 
