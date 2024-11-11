from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# List all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

# Detail view for a specific task
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})

# Update an existing task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = request.POST.get('completed') == 'on'
        task.save()
        return redirect('task_list')
    return render(request, 'task/task_form.html', {'task': task})

# Create a new task
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'task/task_form.html')

# Delete a task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')