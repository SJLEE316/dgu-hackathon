from django.urls import path
from .views import *

app_name="list"
urlpatterns = [
    path('address', address, name="address"),
    path('mypage', mypage, name="mypage"),
    path('login', login, name="login"),
]