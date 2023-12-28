from django.dispatch import receiver
from django.db.models.signals import post_save
from environmentalData.models import EnviromentalData
from enviromentalAlert.models import EnvironmentalAlert
from Register.models import CustomUser
from django.shortcuts import render
from communityReport.models import CommunityReport
from EducationalResource.models import EducationalResource

from Register.models import CustomUser

# models.py (environmentalData)
from django.db import models
from Register.models import CustomUser



# signals.py
from django.dispatch import receiver
from django.db.models.signals import post_save
from environmentalData.models import EnviromentalData
from enviromentalAlert.models import EnvironmentalAlert
from Register.models import CustomUser
from django.shortcuts import render
from Register.models import CustomUser
from score.models import Score


@receiver(post_save, sender=EnviromentalData)
def check_environment(sender, instance, created, **kwargs):
    user = instance.user
    print(user)
    if user:
        # Fetch the CustomUser object
        custom_user = CustomUser.objects.get(id=user.id)

        if (
            instance.humidity is not None
            and instance.humidity >= custom_user.threshold_humidity
        ):
            EnvironmentalAlert.objects.get_or_create(
                user=user,
                message=f"High humidity alert at {instance.timestamp}  Humidity value is {instance.humidity}",
            )

        if (
            instance.water_quality is not None
            and instance.water_quality >= custom_user.threshold_water_quality
        ):
            EnvironmentalAlert.objects.get_or_create(
                user=user,
                message=f"High water quality alert at {instance.timestamp}  Water quality value is {instance.water_quality}",
            )

        if (
            instance.temperature is not None
            and instance.temperature >= custom_user.threshold_temperature
        ):
            EnvironmentalAlert.objects.get_or_create(
                user=user,
                message=f"High temperature alert at {instance.timestamp}  temperature value is {instance.temperature}",
            )


@receiver(post_save, sender=EnviromentalData)
def update_sustainability_score(sender, instance, created, **kwargs):
    if created:
        user = CustomUser.objects.get(id=instance.user.id)
        user_score, created = Score.objects.get_or_create(user=user)
        user_score.sustainability_score += 1
        user_score.save()

@receiver(post_save, sender=EducationalResource)
def update_sustainability_score_education(sender, instance, created, **kwargs):
    if created:
        user = CustomUser.objects.get(id=instance.user.id)
        user_score, created = Score.objects.get_or_create(user=user)
        user_score.sustainability_score += 5
        user_score.save()

@receiver(post_save, sender=CommunityReport)
def update_sustainability_score_community(sender, instance, created, **kwargs):
    if created:
        user_score, created = Score.objects.get_or_create(user=instance.user)
        user_score.sustainability_score += 2  # Adjust scoring logic as needed
        user_score.save()
