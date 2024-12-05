from django import forms
from .models import EmployeeModel
from .models import Product

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = [
            'emp_name',
            'emp_feedback',
        ]

class ProductForm(forms.ModelForm): # links the form to the Products And specifies which field to include
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'stock',
            
        ] 