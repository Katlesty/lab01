from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome")

def sumar(request,a,b):
    res = a + b
    return HttpResponse("La suma de %s + %s es %s" % (a, b, res))

def restar(request,a,b):
    res = a -b 
    return HttpResponse("La resta de %s - %s es %s" % (a,b,res))

def multiplicar(request,a,b):
    res = a * b 
    return HttpResponse("La multiplicación de %s x %s es %s" % (a,b,res))

