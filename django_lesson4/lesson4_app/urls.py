from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', beginner_View, name='beginner_url'),
    path('employees/<int:count>', get_employees_View, name='get_employees_url'),
    path('dep/<int:idisi>', get_dependents_View, name="qarindosh_url"),
]
