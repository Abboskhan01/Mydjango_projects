from django.urls import path
from . views import *


urlpatterns = [
    path('', get_employess, name='employess_list')
]
