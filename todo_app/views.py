from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo_app.models import Task

# Create your views here.
def add_task(request):
    new_task = request.POST['task']
    Task.objects.create(task=new_task)
    return redirect('home')