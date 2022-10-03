from django.db import models

# Create your models here.

class User(models.Model):
    GENDER ={
    ("1", "male"),
    ("2", "female")
    }
    u_fname=models.CharField(max_length=100)
    u_lname=models.CharField(max_length=100)
    u_add1=models.TextField()
    u_add2=models.TextField()
    u_email=models.EmailField()
    u_contact=models.IntegerField()
    u_pan_number=models.IntegerField()
    u_dob=models.DateField()
    u_gender=models.CharField(max_length=100 ,choices=GENDER)

class Accounts(models.Model):
    ATYPE={
    ("1", "Saving"),
    ("2", "Current")
    }
    u_acc_number=models.CharField(max_length=100)
    u_acc_type=models.CharField(max_length=100 ,choices=ATYPE)
    u_acc_balance=models.FloatField()
    u_acc_opendate=models.DateTimeField(default =u_acc_opendate.now, blank = True)

class Cards(models.Model):
        