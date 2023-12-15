from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=150)
    created = models.DateTimeField(default=timezone.now)





