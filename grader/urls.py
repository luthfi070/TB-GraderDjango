from django.urls import path
from django.conf.urls import url
from .views import home, loginView,logoutView,register, identif
from . import views 

urlpatterns = [
    path('', views.home, name="home"), 
    url(r'^/login/$', loginView, name="login"),
    url(r'^/$', logoutView, name='logout'),
    url(r'^signup$', register, name='signup'),
    url(r'^/identify$', identif, name='iden'),
]