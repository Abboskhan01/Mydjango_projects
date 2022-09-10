from django.urls import path
from . import views


urlpatterns = [
    path('', views.seasonsVIEW, name='seasons'),
    path('winter/', views.winterVIEW, name='winter'),
    path('spring/', views.springVIEW, name='spring'),
    path('summer/', views.summerVIEW, name='summer'),
    path('autumn/', views.autumnVIEW, name='summer'),
]
