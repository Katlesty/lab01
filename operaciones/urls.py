from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sumar/<int:a>/<int:b>/', views.sumar, name='sumar'),
    path('restar/<int:a>/<int:b>/', views.restar, name='restar'),
    path('multiplicar/<int:a>/<int:b>/', views.multiplicar, name='multiplicar'),
]
