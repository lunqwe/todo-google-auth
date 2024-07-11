from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    owner = owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.Charfield(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.owner.username} - {self.title} ({self.created_at})'
