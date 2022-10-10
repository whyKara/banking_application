from django.db import models


# Create your models here.

class User(models.Model):
    GENDER ={
    ("1", "male"),
    ("2", "female"),
    ("3", "Other")
    }
    u_ID=models.AutoField(primary_key=True)
    u_fname=models.CharField(max_length=100)
    u_lname=models.CharField(max_length=100)
    u_add1=models.TextField()
    u_add2=models.TextField()
    u_email=models.EmailField()
    u_contact=models.IntegerField()
    u_pan_number=models.IntegerField()
    u_dob=models.DateField()
    u_gender=models.CharField(max_length=100 ,choices=GENDER)

    def __str__(self):
        return self.title

class Accounts(models.Model):
    ATYPE={
    ("1", "Saving"),
    ("2", "Current")
    }
    u_acc_number=models.CharField(max_length=100)
    u_acc_type=models.CharField(max_length=100 ,choices=ATYPE)
    u_acc_balance=models.FloatField()
    u_acc_opendate=models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title

class Cards(models.Model):
    CTYPE={
    ("1", "debit"),
    ("2", "credit")
    }
    u_card_number=models.CharField(max_length=100)
    u_card_type=models.CharField(max_length=100 ,choices=CTYPE)
    u_card_limit=models.IntegerField()
    u_card_pin=models.CharField(max_length=100)
    def __str__(self):
        return self.title


        