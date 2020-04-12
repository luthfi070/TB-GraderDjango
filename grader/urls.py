from django.urls import path
from django.conf.urls import url
from .views import home, loginView,logoutView
from . import views 

urlpatterns = [
    path('', views.home, name="home"), 
    url(r'^login/$', loginView, name="login"),
    url(r'^/$', logoutView, name='logout'),
]