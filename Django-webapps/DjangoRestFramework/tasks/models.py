from django.db import models

# Create your models here.
class Tasks(models.Model):
    title =models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name