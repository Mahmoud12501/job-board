from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import os

# help function
def upload_img(instance,file_name):
    img_name,ext=file_name.split(".")
    
    return "accounts/%s.%s"%(instance.id,ext)

def phone_validat(value):
    if not len(value)==11:
        raise ValidationError(u'Un valid number.')

def validate_file_extension(value):
    ext=os.path.splitext(value.name)[1]
    valid_ext=['.pdf']
    if not ext in valid_ext:
        raise ValidationError(u'Unsupported file extension.')


    
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to= upload_img)
    job=models.CharField(max_length=100,null=True,blank=True)
    website=models.URLField()
    cv=models.FileField(validators=[validate_file_extension],upload_to="cv/",null=True,blank=True)
    DOB=models.DateField(verbose_name="date of birth",null=True,blank=True)
    gender=models.CharField(max_length=20,choices=(('male','male'),('female','female')),null=True,blank=True)
    phone_number= models.CharField(validators=[ RegexValidator(regex=r'^(010|011|012|015)\d{8}$',message="egyption number please")],max_length=11,null=True,blank=True,unique=True)
    
    def __str__(self) -> str:
        return self.user