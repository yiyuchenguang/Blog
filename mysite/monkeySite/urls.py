from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.first),
    # url(r'register/$',views.register),
    # url(r'register_handle/$',views.register_handle),
    # url(r'register_exist/$',views.register_exist),
    # url(r'login/$',views.login),
    # url(r'login_handle/$',views.login_handle),
    # url(r'info/$', views.info),
    url(r'capl_des/$', views.capl_des),
    url(r'capl_des_handle/$', views.capl_des_handle),

    url(r'html_to_doors/', views.html_to_doors),
    url(r'html_to_doors_handle/', views.html_to_doors_handle),
]