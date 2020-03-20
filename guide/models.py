
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Guide(models.Model):
                name=models.CharField(max_length=70)
                image=models.ImageField(upload_to='images/')
                fare=models.IntegerField(default=0)

                contact=models.IntegerField(default=0)

                
                exp=models.IntegerField(default=0)
