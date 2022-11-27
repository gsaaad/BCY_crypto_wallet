from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
    
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length= 50)
#     user_name = models.CharField(max_length= 12)
#     email = models.CharField(max_length=30,unique=True)
#     password = models.CharField(min_length=8, max_length=64)
#     wallet = []
    

class UserProfileInfo(models.Model):
    # create relationship 
    user = models.OneToOneField(User)
    
    # add additional attributes
    # picture = models.ImageField(upload_to='profile_pics')
    
    def __str__(self):
        
        return self.user.username
    
