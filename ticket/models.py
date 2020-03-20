
from django.db import models

class Ticket(models.Model):
    fname=models.CharField(max_length=70)
    lname=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    number=models.IntegerField(default=0)
    age=models.IntegerField(default=18)
    price=models.IntegerField(default=200)
    gender=models.CharField(max_length=15)
    city=models.CharField(max_length=70)
    country=models.CharField(max_length=70)
    pincode=models.IntegerField(default=000000)
