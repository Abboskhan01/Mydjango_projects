from django.shortcuts import render
from .models import Employees, Dependents
from django.http import HttpResponse
from django.db.models import Min


def start_View(request):
    return render(request, 'main.html')


def get_employees(request, employees_count):
    queryset = Employees.objects.all()[:employees_count]
    return render(request,'employees.html', {"EMPLOYEES_Count":queryset})

