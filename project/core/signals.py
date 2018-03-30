from .models import Student, University
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Student)
def index_post(sender, instance, **kwargs):
    instance.indexing()


@receiver(post_save, sender=University)
def university_post(sender, instance, **kwargs):
    instance.indexing()

