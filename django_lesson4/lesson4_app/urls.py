from django.urls import path
from django.http import HttpResponse
from .views import get_dependents, get_max_salary_employess, index_page

urlpatterns = [
    path('', index_page, name='index_page'),

]
