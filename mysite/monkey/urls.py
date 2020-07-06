from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.first),
    url(r'capl_des/$', views.capl_des),
    url(r'capl_des_handle/$', views.capl_des_handle),
    url(r'html_to_doors/', views.html_to_doors),
    url(r'html_to_doors_handle/', views.html_to_doors_handle),
]