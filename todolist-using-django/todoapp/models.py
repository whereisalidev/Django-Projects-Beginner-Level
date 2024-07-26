from django.db import models
from django.db.models import CharField, BooleanField, DateTimeField

class Todo(models.Model):
    title = CharField(max_length=100)
    completed = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
