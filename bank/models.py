from pickle import TRUE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# class User(models.Model):
#     u_id = models.AutoField(primary_key=True)
#     u_fname = models.CharField(max_length=20)
#     u_lname = models.CharField(max_length=20)
#     u_add_l1 = models.TextField()
#     u_add_l2 = models.TextField()
#     u_email = models.EmailField()
#     u_password = models.CharField(max_length=20)
#     u_contact = models.IntegerField()
#     u_pancd = models.CharField(max_length=20)
#     u_doc = models.DateField()
#     u_isemp = models.BooleanField()

class Account(models.Model):
    acc_no = models.CharField(max_length=20, primary_key =True)
    cc_type = models.CharField(max_length=20)
    acc_balance = models.FloatField()
    acc_opendate = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.acc_no

    def get_absolute_url(self):
        return reverse('account-detail', kwargs={'pk': self.pk})

class Card(models.Model):
    c_id = models.CharField(max_length=20, primary_key =True)
    c_type = models.CharField(max_length=10)
    c_pin = models.IntegerField()
    c_limit = models.IntegerField()
    c_doc = models.DateTimeField(auto_now_add=True)
    acc_c = models.ForeignKey(User, on_delete=models.CASCADE)
    


class Transaction(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_facc = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='from_account')
    t_tacc = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='to_account')
    t_ammount = models.FloatField()
    t_doc = models.DateTimeField(auto_now_add=True)
    t_status = models.BooleanField(null=True)
    t_revert_req = models.BooleanField(null=TRUE)


# class user_acc(models.Model):
#     u_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     a_id = models.ForeignKey(Account, on_delete=models.CASCADE)
#     status = models.BooleanField()


# class acc_cards(models.Model):
#     a_id = models.ForeignKey(Account, on_delete=models.CASCADE)
#     c_id = models.ForeignKey(Cards, on_delete=models.CASCADE)
#     status = models.BooleanField()
