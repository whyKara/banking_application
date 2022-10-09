from django.shortcuts import render, redirect
from django.http import HttpResponse
from bank.models import Transaction
from django.contrib.auth.forms import UserCreationForm
from .froms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'emp_bank/e_dashboard.html', context)


# def home(request):
#     # return render(request, 'bank/base.html')
#     return HttpResponse('<h1>addwfawf</h1>')

@login_required
def revert_notofi(request):
    context = {
        'transactions': Transaction.objects.filter(t_revert_req = True)
    }
    return render(request, 'emp_bank/e_revert_notifi.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'emp_bank/u_register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
