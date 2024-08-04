from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)
    
    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)

def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        if 'complete' in request.POST:
            task.complete = not task.complete
            task.save()
        else:
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
        return redirect('/todo/list')  # Redirect to the main list view
    
    context = {'form': form}
    return render(request, 'list.html', context)

def deleteTask(request, pk):
    item = get_object_or_404(Task, id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/todo/list')  # Redirect to the main list view
    
    context = {'item': item}
    return render(request, 'list.html', context)
