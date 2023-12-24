from django.db import models
from Register.models import CustomUser

# eco_track/models.py


class CommunityReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    report_type = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"Report {self.id} - {self.report_type} in {self.city} by {self.user.username}"

    class Meta:
        verbose_name_plural = "CommunityReports"
