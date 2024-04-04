from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    dob = models.DateField()
    profile = models.ImageField(upload_to='shop/profile')
    phone = models.CharField(max_length=15)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'dob', 'phone']

    def __str__(self):
        return self.email

class UserDetail(models.Model):
    name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50) 
    dob = models.DateField()
    profile = models.ImageField(upload_to='shop/profile')
    phone = models.CharField(max_length=15)