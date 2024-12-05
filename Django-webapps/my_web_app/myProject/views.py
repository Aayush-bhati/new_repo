# from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import EmployeeModel
from django.shortcuts import (render,redirect,get_object_or_404,
                             HttpResponseRedirect)

from .models import Product
from .forms import ProductForm


def index(request):

    return HttpResponse("Hello Folks!!")

def create_product(request): # create view for product
    context ={ }
    form = ProductForm(request.POST or None) # Handle the form submission
    if form.is_valid():   # validate and save the form
        form.save()
    context['form'] = form # pass form to template
    return render(request,"create_product.html",context)

# Create  views for employee
def create_view(request):
    context ={ }
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request,"create_view.html",context)

def list_product(request):  # list of products
    context = { }
    context['dataset'] = Product.objects.all()
    return render(request,"list_product.html",context)

# list employees
def list_view(request):
    context={}
    context['dataset'] = EmployeeModel.objects.all()

    return render(request,"list_view.html",context)

def product_detail(request,id):  #detail of given product
    context ={}
    context["data"] = Product.objects.get(id=id)
    return render(request,"product_detail.html",context)


def detail_view(request,id):   #detail of specific employee
    context={}

    context["data"] = EmployeeModel.objects.get(id=id)

    return render(request,"detail_view.html",context)


def update_product(request,id):  #updating the product values
    context ={}
    obj = get_object_or_404(Product,id=id)
    form = ProductForm(request.POST or None,instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/detail/"+id)
    context["form"] = form
    return render(request,"update_product.html",context)

def update_view(request,id):   # updatingthe employee values
    context={}
    obj = get_object_or_404(EmployeeModel,id=id)
    form = EmployeeForm(request.POST or None,instance =obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/detail/"+id)
    context["form"] = form

    return render(request,"update_view.html",context)

def delete_product(request,id):
    context ={}
    obj = get_object_or_404(Product, id =id)
    if request.method =='POST':
        obj.delete()
        return HttpResponseRedirect("/products_list")
    return render(request,"delete_product.html",context)

def delete_view(request,id):
    context = {}
    obj = get_object_or_404(EmployeeModel, id = id)

    if request.method =='POST':
        obj.delete()
        return HttpResponseRedirect("/list")
    return render(request,"delete_view.html",context)