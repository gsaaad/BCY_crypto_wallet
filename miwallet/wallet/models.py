from django.db import models
from django.contrib.auth.models import User
# Create your models

# User model has first name, last last, email,date of birth and wallet
class MongoDBUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    wallet_address = models.CharField(max_length=34, blank=True)
    

    
    

