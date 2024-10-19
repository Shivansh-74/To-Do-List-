from django.db import models



# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)