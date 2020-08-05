from django.urls import path
from .views import address, fax

app_name="list"
urlpatterns = [
    path('address', address, name="address"),
    path('fax', fax, name="fax"),
]