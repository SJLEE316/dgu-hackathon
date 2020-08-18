from django.shortcuts import render

# Create your views here.

def address(request):
    return render(request, 'list/address.html')

def mypage(request):
    return render(request, 'list/mypage.html')

def login(request):
    return render(request, 'list/login.html')    