from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Todo(models.Model):
    title = models.CharField(max_length=120, default='')
    description = models.CharField(max_length=30)
    done = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    class Meta:
        ordering = ["-done"]  # ordering by the created field



