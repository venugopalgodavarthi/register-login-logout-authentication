from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class registermodel(User):
    li=[['MALE','Male'],['FEMALE','Female']]
    gender=models.CharField(max_length=30,choices=li)
    age=models.IntegerField()
    phone=models.BigIntegerField()
    
