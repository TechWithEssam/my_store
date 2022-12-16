from .utils import slugify_name_of_product
from .models import Product, Sales, OrderPlaced
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import datetime
from .utils import slug_code_custom_orders

def post_save_slug_name_product(sender, instance, created, **kwargs) :
    if created :
        slugify_name_of_product(instance, save=True)
post_save.connect(post_save_slug_name_product, sender=Product)


def post_save_sales_buyer(instance, created, sender, **kwargs) :
    if created :
        Sales.objects.create(
            user_order= instance.user,
            product=instance.product,
            quantity=instance.quantity,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            address=instance.address,
            address2=instance.address2,
            country=instance.country,
            state=instance.state,
            zip_code=instance.zip_code,
            status=instance.status,
            slug=instance.slug
        )

post_save.connect(post_save_sales_buyer, sender=OrderPlaced)


def pre_save_change_product_status(sender, instance, **kwargs) :
    if instance.slug is None :
        instance.slug = slug_code_custom_orders()
    slug = instance.slug
    try :
        obj = Sales.objects.filter()
    except :
        obj = None
    if obj :
        for item in obj :
            if item.slug == slug and item.user_order == instance.user:
                item.status = instance.status
                item.save()
pre_save.connect(pre_save_change_product_status, sender=OrderPlaced)