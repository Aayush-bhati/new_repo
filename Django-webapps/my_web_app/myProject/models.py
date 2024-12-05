from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_feedback = models.TextField()

    def __str__(self):
        return self.emp_name
    
class Product(models.Model):   # creating app for Product
    name = models.CharField(max_length=200)
    description =models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places =2)
    stock = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # defines how an object is represnted as a string
        return self.name