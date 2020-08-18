from django.urls import path
from .views import *

app_name= "reviews"
urlpatterns = [
    path('main', main, name="main"),
    path('new/', new, name="new"),
    path('new2/', new2, name="new2"),
    path('create/', create, name="create"),   
    path('show/<int:id>', show, name="show"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]