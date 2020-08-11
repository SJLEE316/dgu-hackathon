from django.urls import path
from .views import *

app_name="list"
urlpatterns = [
    path('address', address, name="address"),
    path('fax', fax, name="fax"),
    path('login', login, name="login"),
]