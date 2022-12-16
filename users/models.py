from django.db import models
from django.db.models.signals import post_save
from datetime import date
from django.contrib.auth.models import AbstractUser


class Subscribe(models.Model) :
    email = models.EmailField(max_length=60)
    def __str__(self) :
        return str(self.email)


GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Custom","Custom")
)
class User(AbstractUser) :
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=6, blank=True, null=True)

class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=120, blank=True)
    avatar = models.ImageField(upload_to="profiles", default="profiles/avatar.png")
    nationality = models.CharField(max_length=120, blank=True)
    is_buyer = models.BooleanField(default=False)

    @property
    def user_age(self) :
        if self.user.date_of_birth is not None :
            user_age = date.today().year - self.user.date_of_birth.year
            return user_age
    def __str__(self) :
        return f"profile of {self.user.username}"
    
    @property
    def avatar_url(self) :
        try :
            url = self.avatar.url
        except :
            url = None
        return url
    
    @property
    def total_price_cart(self) :
        cart = self.cart_set.all()
        total = sum([item.total_cart_price for item in cart])
        return total
    