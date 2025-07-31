from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
    
class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    total = models.CharField(max_length=50, default="0")

    def __str__(self):
        return self.items
