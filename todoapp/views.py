from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from . forms import TodoFrom
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class TaskListview(ListView):
    model=Task
    template_name = 'index.html'
    context_object_name = 'task1'

class TaskDetaleview(DetailView):
    model = Task
    template_name = 'detale.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

class TaskDeleteview(DeleteView):
     model = Task
     template_name = 'delete.html'
     success_url = reverse_lazy('cbvindex')
     def get_success_url(self):
          return  reverse_lazy('cbvdetale',kwargs={'pk':self.object.id})
# Create your views here.

def index(request):
    task1=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority,date=date)
        task.save()
    return render(request, 'index.html',{'task1': task1})

def delete(request,taskid):
    if request.method == 'POST':
        task = Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render (request,'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form = TodoFrom(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'task': task})


