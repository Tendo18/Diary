from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Diary(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='diary', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.title)   

class Profile(models.Model):
    GENDER = [
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]
    fullname = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 20)
    gender = models.CharField(max_length=6, choices=GENDER)
    image = models.ImageField(upload_to='profile', blank=True, null = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.user.fullname)


    

    