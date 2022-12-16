from django.db.models.signals import post_save, pre_save
from .models import User, Profile



def post_save_create_profile(sender, created, instance, **kwargs) :
    if created :
        Profile.objects.create(user=instance)
post_save.connect(post_save_create_profile, sender=User)