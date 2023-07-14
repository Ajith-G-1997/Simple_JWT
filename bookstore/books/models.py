from django.db import models
from django.contrib.auth.models import AbstractUser



class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title



class User(AbstractUser):
    email = models.EmailField(unique=True) 
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50) 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name',"last_name"]
    
    def __str__(self):
        return self.email




# User._meta.get_field('groups').remote_field.related_name = 'books_user_set'
# User._meta.get_field('user_permissions').remote_field.related_name = 'books_user_set'
   

