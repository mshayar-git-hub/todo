from django.shortcuts import render
from todo_app.models import Task

def home(request):
    tasks = Task.objects.filter(is_complete = False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_complete = True).order_by('-updated_at')
    context = {
        'tasks' : tasks ,
        'completed_task' : completed_task,
    }
    return render(request, 'index.html' , context)