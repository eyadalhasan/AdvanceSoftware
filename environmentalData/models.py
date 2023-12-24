from django.db import models
from Register.models import CustomUser


class EnviromentalData(models.Model):
    user = models.ForeignKey(
        CustomUser, null=True, on_delete=models.CASCADE, blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    air_quality = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    water_quality = models.FloatField()
    biodiversity_metrics = models.FloatField()
    city = models.CharField(max_length=255, blank=True, null=True, default="")

    def __str__(self):
        return f"{self.city} - {self.temperature}"

    class Meta:
        verbose_name_plural = "Enviromental Data"
