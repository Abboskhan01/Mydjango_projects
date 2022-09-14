from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees


def get_employess(request):
    queryset = Employees.objects.only('first_name')
    print("\n", queryset.query)
    str_data = ""
    for i in queryset:
        str_data += f"<li>{i}</li>"
    return HttpResponse(f"<ul>{str_data}</ul>")
