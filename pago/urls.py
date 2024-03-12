from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:p>/<str:h>/',views.pago,name='pago')
]