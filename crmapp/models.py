from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
class CardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    archived = models.BooleanField(default=False)
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)