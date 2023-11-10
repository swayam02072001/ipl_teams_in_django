from django.shortcuts import render
from django.http import HttpResponse

def rohit(request):
    return render(request, 'rohit.html')

def bumrah(request):
    return HttpResponse('<center><h1>Boom Boom Bumrah</center></h1>)')