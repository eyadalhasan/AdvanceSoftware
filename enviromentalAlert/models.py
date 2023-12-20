from django.db import models
from Register.models import CustomUser


class EnvironmentalAlert(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.message}  {self.timestamp}"
