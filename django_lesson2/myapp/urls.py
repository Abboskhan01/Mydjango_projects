from django.urls import path
from . views import authors_list

urlpatterns = [
    path('', authors_list, name='author list'),
]
