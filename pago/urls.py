from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:p>/<int:h>/',views.pago,name='pago')
]