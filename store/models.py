from django.db import models
from accounts.models import Account
from django.utils.text import slugify
from users.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db.models import Q


CATEGORY_CHOICES = (
    ("Men","Men"),
    ("Women","Women"),
    ("Children","Children")
)


class Brand(models.Model) :
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    
    def __str__(self) :
        return self.name
    
    def save(self, *args, **kwargs) :
        if not self.slug :
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Category(models.Model) :
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self) :
        return self.name
    def save(self, *args, **kwargs) :
        if not self.slug :
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)



class ProductQuerySet(models.QuerySet) :
    def search(self, query=None) :
        if query is None or query == "" :
            return self.none()
        lookup = Q(name__icontains=query) | Q(description__icontains=query)| Q(brand__name__icontains=query)| Q(category__name__icontains=query)
        return self.filter(lookup)

class ProductManager(models.Manager) :
    def get_queryset(self) :
        return ProductQuerySet(self.model, using=self._db)
    def search(self, query) :
        return self.get_queryset().search(query=query)

class Product(models.Model) :
    salesman = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=122)
    slug = models.SlugField(blank=True, null=True, unique=True)
    image = models.ImageField(upload_to="products")
    price = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    option = models.CharField(max_length=10, choices=CATEGORY_CHOICES, blank=True, null=True)
    description = models.TextField()
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(70),MinValueValidator(0) ])
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ProductManager()

    @property
    def new_price_after_dicount(self) :
        if self.discount != 0 :
            new_price = self.price - self.price * self.discount / 100
        else :
            new_price = self.price
        return new_price
    
    def __str__(self) :
        return f"{self.name}"
    
    @property
    def detail_product_url(self) :
        return reverse("store:detail", kwargs={"slug":self.slug})
    
    @property
    def filter_brand_url(self) :
        return reverse("store:filter_brand", kwargs={"slug":self.category.slug,"slug":self.brand.slug})

class Cart(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def total_cart_price(self) :
        if self.product.discount != 0 :
            new_price = self.product.price - self.product.price * self.product.discount / 100
        else :
            new_price = self.product.price
        total = new_price * self.quantity
        return total
    def __str__(self) :
        return f"{str(self.product.name)} {self.total_cart_price}"


STATUS_ORDER_CART = (
    ("tm" , "The request was successful"),
    ("dr","Delivery is underway"),
    ("sdh", "sent delivered handed")
    )


class OrderPlaced(models.Model) :
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, unique=True)
    quantity = models.IntegerField(default=1)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_ORDER_CART, blank=True)

    def __str__(self) :
        return str(self.user)
    
    def total_price_only_one_product(self) :
        return self.product.new_price_after_dicount * self.quantity


class Sales(models.Model) :
    user_order = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    slug = models.SlugField(blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    email= models.EmailField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    @property
    def total_price(self) :
        return self.product.new_price_after_dicount * self.quantity
    def __str__(self) :
        return f"order for {str(self.user_order.user.username)} {self.total_price}"
    
    