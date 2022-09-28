from django.db import models

# Create your models here.
class User (models.Model):
    u_fname=models.CharField(max_length=100)
    u_lname=models.CharField(max_length=100)
    u_add1=models.TextField()
    u_add2=models.TextField()
    u_email=models.EmailField()
    u_contact=models.IntegerField()
    u_pan_number=models.IntegerField()
    u_dob=models.DateField()
    u_gender=models.ChoiceField()

# class Accounts(models.Model):
#     u_Acc_number=models.charfield(max_length=100)
#     u_card_type=