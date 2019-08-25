from utils.unique_slug_field_generator import unique_slug_generator, random_string_generator
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member

@receiver(post_save, sender=Member)
def object_post_save_reciever(sender, instance, created, **kwargs):

        if not instance.slug:

                slug = unique_slug_generator(instance)

                instance.slug = slug

                instance.save()

