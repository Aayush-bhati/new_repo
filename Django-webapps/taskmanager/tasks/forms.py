from django import forms
from .models import Task

class TaskForm(forms.ModelForm): 
    # links the forms to Task
    class Meta:              # and specifies which record to include
        model = Task
        fields = [
            'title',
            'description',
            'completed',
            
        ]
