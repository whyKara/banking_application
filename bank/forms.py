from django.forms import ModelForm
from .models import User
from .models import Accounts
from .models import Cards

class UserForm(ModelForm):
    class meta:
        model=User
        fields='__all__'

class AccountsForm(ModelForm):
    class meta:
        model=Accounts
        fields='__all__'        

class CardsForm(ModelForm):
    class meta:
        model=Cards
        fields='__all__'    