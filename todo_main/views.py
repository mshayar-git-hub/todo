from django.shortcuts import render
from todo_app.models import Task

def home(request):
    tasks = Task.objects.filter(is_complete = False).order_by('-updated_at')
    context = {
        'tasks' : tasks ,
    }
    return render(request, 'index.html' , context)