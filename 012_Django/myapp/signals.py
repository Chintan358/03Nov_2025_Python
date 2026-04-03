from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import *


@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):
    if created:
        print(f"Student {instance.name} created!")