from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import os
# Create your models here.

job_ty=(
    ('full time','full time'),
    ('part time','part time'),
)
# help function
def upload_img(instance,file_name):
    img_name,ext=file_name.split(".")

    return "job/%s.%s"%(instance.id,ext)

def validate_file_extension(value):
    ext=os.path.splitext(value.name)[1]
    valid_ext=['.pdf']
    if not ext in valid_ext:
        raise ValidationError(u'Unsupported file extension.')



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

    owner=models.ForeignKey(User,related_name="job_owner",on_delete=models.CASCADE)
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
    slug=models.SlugField(max_length=100,blank=True,null=True)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title) 
        super(Job,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.title


class Applicants(models.Model):
    job=models.ForeignKey(Job,related_name='applay_job',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    website=models.URLField()
    cv=models.FileField(validators=[validate_file_extension],upload_to="cv/")
    coverletter=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name