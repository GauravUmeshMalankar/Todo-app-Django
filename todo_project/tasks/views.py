from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
        messages.success(request, f"✅ Task '{title}' added successfully!")
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    messages.success(request, f"🎉 Task '{task.title}' marked as completed!")
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    title = task.title
    task.delete()
    messages.warning(request, f"🗑️ Task '{title}' deleted successfully!")
    return redirect('task_list')