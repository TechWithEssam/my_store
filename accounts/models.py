from django.db import models
from users.models import Profile



class Account(models.Model):
	buyer = models.OneToOneField(Profile, on_delete=models.CASCADE)
	logo = models.ImageField(upload_to="accounts", default="accounts/logo.png")
	url = models.SlugField(blank=True, null=True, unique=True)
	name = models.CharField(max_length=120)
	Brief = models.TextField()
	email = models.EmailField()
	followers = models.ManyToManyField(Profile, blank=True, related_name="followers")
	address = models.CharField(verbose_name="Address",max_length=100)
	town = models.CharField(verbose_name="Town/City",max_length=100)
	county = models.CharField(verbose_name="County",max_length=100)
	country = models.CharField(verbose_name="Country",max_length=100)
	longitude = models.CharField(verbose_name="Longitude",max_length=50)
	latitude = models.CharField(verbose_name="Latitude",max_length=50)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	def __str__(self) :
		return f"account for {self.buyer.user.username} {self.name}"
	
	@property
	def all_followers(self) :
		return self.followers.count()
	
	@property
	def my_products(self) :
		product = self.product_set.all()
		return product
	
	@property
	def my_products_count(self) :
		return self.my_products.count()
	

