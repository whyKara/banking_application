from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    return render(request, 'emp_bank/base.html')


def home(request):
    # return render(request, 'bank/base.html')
    return HttpResponse('<h1>addwfawf</h1>')
