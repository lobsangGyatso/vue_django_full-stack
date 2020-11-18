from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=122)

    def __str__(self):
        return self.title

class DepartmentStore(models.Model):
    title = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ShopItem(models.Model):
    title = models.CharField(max_length=122)
    dept = models.ForeignKey(DepartmentStore, on_delete = models.CASCADE)
    price = models.IntegerField()
    timestamp =models.DateTimeField(default=now)
    picture = models.ImageField(upload_to="store/images/", max_length=255, null = True, blank = True)

    def __str__(self):
        return self.title

class orderItem(models.Model):
    # orderuser  = models.ForeignKey(User,on_delete=models.CASCADE)
    item  = models.ForeignKey(ShopItem,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)

# class Order(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     item = models.ManyToManyField(orderItem)