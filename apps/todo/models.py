from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    period_of_execution = models.DurationField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
