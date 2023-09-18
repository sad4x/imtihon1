from django.shortcuts import render
from .models import ToDo

def todo(request):
    context = {
        "todos": ToDo.objects.all()
    }
    return render(request, 'template.html', context)

def adding(request):
    return render(request, 'adding.html')