from django.db import models

# Create your models here.

class add_course(models.Model):
    c_code=models.CharField(max_length=50)
    c_name=models.CharField(max_length=255)
    c_des=models.CharField(max_length=255)
    c_du=models.CharField(max_length=200)
    c_fee=models.IntegerField()

class add_student(models.Model) :
    s_code=models.CharField(max_length=255)
    s_name=models.CharField(max_length=255)
    s_add=models.CharField(max_length=255)
    s_age=models.IntegerField()
    s_gen=models.CharField(max_length=255)
    s_mail=models.EmailField()
    





    
