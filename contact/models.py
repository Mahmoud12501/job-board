from django.db import models

# Create your models here.
class Info(models.Model):
    adress=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)