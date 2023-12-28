from django.db import models


class EducationalResource(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        verbose_name_plural = "EducationalResources"

    def __str__(self):
        return self.title
