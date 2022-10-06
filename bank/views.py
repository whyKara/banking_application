from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Card, Transaction
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)


def account(request):
    context = {
        'accs': Account.objects.all()
    }
    return render(request, 'bank/u_account.html', context)



class AccountListView(ListView):
    model = Account
    template_name = 'bank/u_account.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'accs'
    ordering = ['-date_posted']


class AccountDetailView(DetailView):
    model = Account


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Account
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def card(request):
    context = {
        'cards': Card.objects.all()
    }
    return render(request, 'bank/u_cards.html', context)


def transaction(request):
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'bank/u_transaction.html', context)


def home(request):
    # return render(request, 'bank/base.html')
    return HttpResponse('<h1>sjyfsuyf</h1>')
