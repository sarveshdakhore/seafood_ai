from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path for home /home
    path('home/', views.home, name='home'),
]