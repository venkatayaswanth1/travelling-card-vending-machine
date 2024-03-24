from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, mobile=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, mobile=mobile)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, mobile=None):
        user = self.create_user(username, email, password, mobile)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class user(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    proof = models.ImageField(upload_to='proofs/')
   


