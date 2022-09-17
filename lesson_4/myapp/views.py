from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees, Dependents
from django.db.models import Min
from django.shortcuts import render

def get_max_salary_employees(request,top):
    # queryset = Employees.objects.order_by('-salary')[:top].values_list('first_name','last_name','salary')
    queryset = Employees.objects.all().order_by('-salary')[:top]
    # print(queryset[0].salary)
    return render(request,"max_salary.html",{'max_salary': queryset})

def get_dependents(request, employee_id):
    queryset = Dependents.objects.all().filter(employee=employee_id)
    employee = Employees.objects.get(employee_id=employee_id)
    context = {"deps":queryset,"employee":employee}
    return render(request,"dependents.html",context)

def index_page(request):
    return render(request, "index.html")