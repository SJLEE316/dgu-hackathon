from django.shortcuts import render

# Create your views here.

def address(request):
    return render(request, 'list/address.html')

def fax(request):
    return render(request, 'list/fax.html')

def login(request):
    return render(request, 'list/login.html')    