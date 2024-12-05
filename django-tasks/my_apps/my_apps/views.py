from django.http import HttpResponse

from .models import PersonModel
from .forms  import PersonForm

from django.shortcuts import render

def my_world(request):
    return HttpResponse("Hi! Welcome to My App!!")

def create_view(request):
    context ={}
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request,"create_view.html",context)


