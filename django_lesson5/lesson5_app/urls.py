from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', register_View, name='register_view_urls'),
]
