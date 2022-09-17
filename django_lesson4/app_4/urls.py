from django.urls import path
from .views import start_View, get_employees


urlpatterns =[
   path("", start_View, name='start_view'),
   path('employees/<int:employees_count>', get_employees, name='get_xodimlar',)
]
