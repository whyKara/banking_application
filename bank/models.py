from django.db import models

# Create your models here.
class User (models.Model):
    u_fname=models.charfield(max_length=100)
    u_lname=models.charfield(max_length=100)
    u_add1=models.textfield()
    u_add2=models.textfield()
    u_email=models.EmailField()
    u_contact=models.IntegerField()
    u_pan_number=models.IntegerField()
    u_dob=models.DateField()
    U_gender=models.choiceField()

# class Accounts(models.Model):
#     u_Acc_number=models.charfield(max_length=100)
#     u_card_type=