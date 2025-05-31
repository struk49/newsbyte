from django.urls import path
from . import views

urlpatterns = [
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('cookies/', views.cookies, name='cookies'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
