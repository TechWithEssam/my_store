from users.models import Profile
from .models import Account
from django.db.models.signals import pre_delete, pre_save
from store.models import OrderPlaced
from django.dispatch import receiver
from uuid import uuid4


def per_save_modify_create_url_and_active_buyer(instance, sender, **kwargs) :
    if instance.url is None :
        instance.url = str(uuid4())[:20].replace("-",'')
    obj = Profile.objects.get(user=instance.buyer.user)
    if obj.is_buyer == False :
        obj.is_buyer = True
        obj.save()
pre_save.connect(per_save_modify_create_url_and_active_buyer, sender=Account)

def pre_delete_deactived_buyer(sender, instance, **kwargs) :
    obj = Profile.objects.get(user=instance.buyer.user)
    obj.is_buyer = False
    obj.save()
pre_delete.connect(pre_delete_deactived_buyer, sender=Account)