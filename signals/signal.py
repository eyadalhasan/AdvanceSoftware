from django.dispatch import receiver
from django.db.models.signals import post_save
from environmentalData.models import EnviromentalData
from enviromentalAlert.models import EnvironmentalAlert
from Register.models import CustomUser


@receiver(post_save, sender=EnviromentalData)
def check_environment(sender, instance, **kwargs):
    """
    Signal handler to check humidity and water quality values and create alerts if conditions are met.
    """

    city_users = CustomUser.objects.filter(city=instance.city)

    for user in city_users:
        print(user.city)
    if instance.humidity == 10:
        for user in city_users:
            EnvironmentalAlert.objects.create(
                user=user,
                message=f"High humidity alert at {instance.timestamp}  Humidity value is {instance.humidity}",
            )

    if instance.water_quality >= 9:
        for user in city_users:
            EnvironmentalAlert.objects.create(
                user=user,
                message=f"High water quality alert at {instance.timestamp}  Water quality value is {instance.water_quality}",
            )
