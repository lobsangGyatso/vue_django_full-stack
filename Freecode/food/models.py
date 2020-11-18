from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=122)
    picture = models.ImageField(upload_to="store/images/", max_length=255, null = True, blank = True)

    def __str__(self):
        return self.title


class Center(models.Model):
    name = models.CharField(max_length=22)
    def __str__(self):
        return self.name

class Product(models.Model):
    productname = models.CharField(max_length=122)
    cat = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.IntegerField()
    timestamp =models.DateTimeField(default=now)
    picture = models.ImageField(upload_to="store/images/", max_length=255, null = True, blank = True)

    def __str__(self):
        return self.productname




class orderItem(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    product  = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ManyToManyField(orderItem)

# ifrst we slect the item to add to cart  or order
# ceate the order item 
