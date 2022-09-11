from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^main/(tosh|qash|far)/', views.main, name='uzbekistan'),
    path('global/<str:region>', views.regionsVIEW, name='regions')
]
