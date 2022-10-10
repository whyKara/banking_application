from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
from django.forms import ModelForm
from .models import User
from .models import Accounts
from .models import Cards

class UserForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"
        widgets={
        'u_fname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
		'u_lname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
		'u_add1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Line 1'}),
		'u_add2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Line 2'}),
        'u_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        'u_contact': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
        'u_pan_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pan Card'}),
        'u_dob': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date Of Birth'}),
        'u_gender': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'male/female/other'}),
        }

class AccountsForm(ModelForm):
    class Meta:
        model=Accounts
        fields="__all__"       

class CardsForm(ModelForm):
    class Meta:
        model=Cards
        fields="__all__" 