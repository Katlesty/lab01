from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Bienvenido")

def pago(request,p,h):
    p=float(p)
    h=float(h)
    
    if h<=40:
        res = p*h
        return HttpResponse("El pago de la semana es: %s" % res)
    else:
        res = 2*(p*h)
        return HttpResponse("El pago de la semana es %s" % res)