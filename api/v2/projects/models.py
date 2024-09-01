from django.db import models
from core.models import TimeStampedModel

class Project(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name