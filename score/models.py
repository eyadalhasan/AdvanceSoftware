from django.db import models
from Register.models import CustomUser


class Score(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    sustainability_score = models.IntegerField(default=0)

    def __str__(self):
        return f"Sustainability Score for {self.user.username}"
    

