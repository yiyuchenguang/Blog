from django.contrib import admin
from django.urls import path,include
from . import views

# app_name = 'blog'


urlpatterns = [
    path('', views.index_unlog, name='index_unlog'),
    path('login',views.login,name='login'),
    path('log', views.logsuccess, name='login-success'),
    path('register',views.register,name='register'),
    path('forget', views.forget_password, name='forget'),
    path('reset', views.reset, name='reset'),
    path('log_out', views.reset, name='log_out'),
    path('home', views.home, name='home'),
]
