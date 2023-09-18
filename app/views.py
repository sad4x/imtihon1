from django.shortcuts import render, redirect
from .models import ToDo

def todo(request):
    if request.POST:
        title = request.POST.get('title')
        time = request.POST.get('time')
        desc = request.POST.get('desc')
        status = request.POST.get('status')

        ToDo.objects.create(title=title, time=time, desc=desc,status=status)

    context = {
        "todos": ToDo.objects.all()
    }
    return render(request, 'template.html', context)

def adding(request):
    return render(request, 'adding.html')

def delete(request,id):
    ToDo.objects.get(id=id).delete()
    return redirect('/')

def edit(request, id):
    context = {
        'todo': ToDo.objects.get(id=id)
    }
    return render(request,'edit.html', context)