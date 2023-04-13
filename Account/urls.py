from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('change_pass/', change_pass, name='change_pass'),
    path('registration/', registration, name='registration'),
]
