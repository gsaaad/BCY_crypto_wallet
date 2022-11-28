from django.db import models

# Create your models

# User model has first name, last last, email,date of birth and wallet
class MongoDBUser(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 50)
    user_name = models.CharField(max_length= 12, unique = True)
    date_of_birth = models.DateField()
    
    # password = models.CharField(max_length=12)
    email = models.CharField(max_length=30,unique=True)
    wallet = []
    
    def __str__(self):
        return "Email: %s" % self.email
    
    

