from django.shortcuts import render
from django.http import HttpResponse

def abd(request):
    return render(request, 'abd.html')

def virat(request):
    return HttpResponse('<center><h1>)King Kohli</center></h1>)')