from django.shortcuts import render
from .models import Employees, Dependents


def beginner_View(request):
    return render(request, 'beginner.html')


def get_employees_View(request, count):
    queryset = Employees.objects.all()[:count]
    return render(request, 'get_employees.html', {'employees_list':queryset})


def get_dependents_View(request, idisi):
    xodim = Employees.objects.filter(employee_id=idisi)
    qondoshi = Dependents.objects.get(employee=idisi)
    data = {'qondosh':xodim, 'qondoshligi':qondoshi}
    return render(request, 'get_dependents.html', data)

