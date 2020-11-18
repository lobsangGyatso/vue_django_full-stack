from django.db import models

# Create your models here.
class Reporter(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    headline = models.CharField(max_length=100)
    Reporter = models.ForeignKey(Reporter, on_delete = models.CASCADE)
    picture = models.ImageField(upload_to="store/images/", max_length=255, null = True, blank = True)
    # def __str__(self):
    #     return self.headline 


class Publication(models.Model):
    name = models.CharField(max_length=122)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# multiple model 