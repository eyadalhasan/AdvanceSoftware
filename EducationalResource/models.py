from django.db import models
from Register.models import CustomUser

class EducationalResource(models.Model):
    user = models.ForeignKey(
        CustomUser,
        null=True,
        on_delete=models.CASCADE,
        blank=True,
        related_name="educational_resource",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        verbose_name_plural = "EducationalResources"

    def __str__(self):
        return self.title
