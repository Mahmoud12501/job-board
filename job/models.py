from django.db import models

# Create your models here.

job_ty=(
    ('FT','full time'),
    ('PT','part time'),
)

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Job(models.Model):

    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=job_ty)
    experience=models.IntegerField(default=1)
    jop_describtion=models.TextField(max_length=1000)
    puplish_date=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    Salary=models.DecimalField(max_digits=6,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title