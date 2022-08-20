from django.db import models
import os
# Create your models here.

job_ty=(
    ('full time','full time'),
    ('part time','part time'),
)

def upload_img(instance,file_name):
    img_name,ext=file_name.split(".")

    return "job/%s.%s"%(instance.id,ext)


class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    city=models.CharField(max_length=100)
    countery=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.city

class Job(models.Model):

    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=job_ty)
    experience=models.IntegerField(default=1)
    jop_describtion=models.TextField(max_length=1000)
    puplish_date=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    Salary=models.DecimalField(max_digits=6,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    img=models.ImageField(upload_to= upload_img)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title