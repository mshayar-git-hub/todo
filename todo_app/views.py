from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from todo_app.models import Task

# Create your views here.
def add_task(request):
    new_task = request.POST['task']
    Task.objects.create(task=new_task)
    return redirect('home')


def mark_as_done(request , pk):
    task = get_object_or_404(Task , pk=pk)
    task.is_complete = True
    task.save()
    return redirect('home')    

def mark_as_undone(request , pk):
    task = get_object_or_404 (Task , pk = pk)
    task.is_complete = False
    task.save()
    return redirect('home')

def delete_task(request , pk):
    task = get_object_or_404(Task , pk = pk)
    task.delete()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        updated_task = request.POST.get('task')

        if updated_task:
            task.task = updated_task
            task.save()
            return redirect('home')

    return render(request, 'edit.html', {'task': task})