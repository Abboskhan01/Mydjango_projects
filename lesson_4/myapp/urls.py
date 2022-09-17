from django.urls import path
from .views import get_max_salary_employees, get_dependents,index_page

urlpatterns = [
    path('',index_page,name='index_page'),
    path('salary/<int:top>', get_max_salary_employees, name='employee-list'),
    path('deps/<int:employee_id>', get_dependents, name='deps-list'),

]