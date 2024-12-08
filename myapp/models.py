from django.db import models

# Create your models here.
class Proyect(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    project = models.ForeignKey(Proyect, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}--{self.project}"