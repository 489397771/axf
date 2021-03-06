from django.db import models

# Create your models here.
class Wheel(models.Model):
    img = models.CharField(max_length = 256)
    name = models.CharField(max_length = 64)
    trackid = models.IntegerField()
    isDelete = models.BooleanField(default = False)

class Nav(models.Model):
    img = models.CharField(max_length = 256)
    name = models.CharField(max_length = 64)
    trackid = models.IntegerField()

class mustbuy(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

class shop(models.Model):
    img = models.CharField(max_length = 256)
    name = models.CharField(max_length = 64)
    trackid = models.IntegerField()

class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)


