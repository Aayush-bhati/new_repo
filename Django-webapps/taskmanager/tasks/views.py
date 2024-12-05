from django.shortcuts import (render,redirect,get_object_or_404,
                             HttpResponseRedirect)
from .models import Task
from .forms import TaskForm
# Create your views here.

def create_task(request):   # create view for Tasks
    context ={}
    form = TaskForm(request.POST or None)
    if form.is_valid():
        print("Here")
        form.save()
        return HttpResponseRedirect("/list/")
    context['form'] = form
    print(context)
    return render(request,'create.html',context)


def home(request):  # lists for the task
    context={}
    context['dataset'] = Task.objects.all()
    print(context['dataset'])
    return render(request,'home_view.html',context)

def home_details(request,id): # details of the Tasks
    context={}
    context['data'] = Task.objects.get(id=id)
    return render(request,'detail_view.html',context)

def update_task(request,id):   # doing update operation
    context ={}
    obj = get_object_or_404(Task,id=id)
    form = TaskForm(request.POST or None,instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/detail/"+id)
    context["form"] =form
    return render(request,"update_tasks.html",context)

def delete_task(request,id):  # doing delete operation for tasks
    context ={}
    obj = get_object_or_404(Task,id=id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/list/")
    return render(request,"delete_task.html",context)

