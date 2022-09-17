from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees, Dependents
from django.db.models import Min


def index_page(request):
    return render(request, 'index.html')


def get_max_salary_employess(request, top):
    pass


def get_dependents(request, employe_id):
    pass
