from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self) -> str:
        return self.title
