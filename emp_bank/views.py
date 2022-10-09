from django.shortcuts import render, redirect
from django.http import HttpResponse
from bank.models import Account, Card, Transaction
from django.contrib.auth.forms import UserCreationForm
from .froms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)


@login_required
def dashboard(request):
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'emp_bank/e_dashboard.html', context)

class NewAccountView(LoginRequiredMixin,CreateView):
    model = Account
    fields = ['acc_no', 'cc_type','acc_balance','owner']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewCardView(LoginRequiredMixin,CreateView):
    model = Card
    fields = ['c_id', 'c_type','c_pin','c_limit','acc_c']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
