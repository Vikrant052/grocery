from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=15, unique=True)

    REQUIRED_FIELDS = ['name', 'phone'] 
    USERNAME_FIELD = 'email'  

    def __str__(self):
        return self.email
