from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    age = models.CharField(max_length=20)
    # is_anonymous = models.BooleanField(default=True)
    # is_authenticated = models.BooleanField(default=True)
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['password']

class LoginModel(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    
    def __str__(self):
        return self.email
        