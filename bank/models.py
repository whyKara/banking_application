from django.db import models

# Create your models here.
class create_account (models.Model):
    u_fname=models.charfield(max_length=100)
    u_lname=models.charfield(max_length=100)
    u_Acc_number=models.charfield(max_length=100)
    u_card_type=
    u_email=models.EmailField()
    u_contact=models.IntegerField()
    u_pan_number=models.IntegerField()
    u_dob=models.DateField()
    U_gender=