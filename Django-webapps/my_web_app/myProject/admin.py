from django.contrib import admin

# Register your models here.
from .models import EmployeeModel,Product
admin.site.register(EmployeeModel)
admin.site.register(Product)