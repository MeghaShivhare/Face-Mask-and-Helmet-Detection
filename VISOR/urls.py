from django.contrib import admin
from django.urls import path  
from VISOR import views

urlpatterns = [
    path("", views.index, name='Home'),
    path("about", views.about, name='About'),
    path("contact", views.contact, name='Contact'),
    path("face", views.face, name='Face Detector'),
    path("helmet", views.helmet, name='Helmet Detector'),
    path("terms",views.terms, name='Terms and Conditions'),
]