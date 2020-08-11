from django.urls import path
from .views import *

app_name= "posts"
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('main/', main, name="main"),
    path('main2/', main2, name="main2"),
    path('main3/', main2, name="main3"),
    path('main4/', main2, name="main4"),
    path('main5/', main2, name="main5"),    
    path('show/<int:id>', show, name="show"),
]