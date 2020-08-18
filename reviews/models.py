from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=10)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
