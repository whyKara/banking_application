from tkinter import Widget
from xml.dom.minidom import Attr
from django.forms import ModelForm
from .models import User
from .models import Accounts
from .models import Cards

class UserForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"

class AccountsForm(ModelForm):
    class Meta:
        model=Accounts
        fields="__all__"       

class CardsForm(ModelForm):
    class Meta:
        model=Cards
        fields="__all__" 