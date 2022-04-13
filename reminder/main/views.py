from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': "Головна сторінка", 'tasks': tasks})


def TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'main/delete.html'
    context_object_name = 'task'


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма була неправильною'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)