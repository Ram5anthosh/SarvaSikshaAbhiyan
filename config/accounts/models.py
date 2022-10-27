from django.db import models

# Create your models here.

class Volunteer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    usrname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    instiname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    passwd = models.CharField(max_length=50)
    cpasswd = models.CharField(max_length=50)
    
    def __str__(self):
        return self.usrname
    
