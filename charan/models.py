from django.db import models

# Create your models here.
class Order(models.Model):
   name = models.CharField(max_length=100)
   quantity = models.IntegerField()
   dimensions = models.CharField(max_length=20)
   price = models.IntegerField()
   availability=models.BooleanField()