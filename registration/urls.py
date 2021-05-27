from django.urls import path
from .views import *

urlpatterns = [
    path('',LandingPage, name='LandingPage'),
    path('register/', Register, name='Register'),
    path('aboutus/', Aboutus, name='Aboutus'),
    path('registrations/', Registrations, name='Registrations'),
]