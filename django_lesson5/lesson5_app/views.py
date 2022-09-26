from django.shortcuts import render
from .models import Student


def register_View(request):
    if request.POST:
        model = Student()
        model.first_name = request.POST['first_name']
        model.last_name = request.POST['last_name']
        model.email = request.POST['email']
        model.password = request.POST['password']
        model.course_type = request.POST['course_type']
        model.phone_number = request.POST['phone_number']
        model.save()
    return render(request, 'register.html')
