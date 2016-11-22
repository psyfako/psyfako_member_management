from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Fachschaft(models.Model):
    university_name = models.CharField(max_length=240, blank=True)
    university_type = models.CharField(max_length=3, blank=True)
    city = models.CharField(max_length=240, blank=True)
    mail = models.EmailField(max_length=254)
    

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # extendet user stats
    address_street       = models.CharField(max_length=240, blank=True)
    address_streetnumber = models.IntegerField()
    address_city         = models.CharField(max_length=240, blank=True)
    address_citycode     = models.IntegerField()
    
    mobilephone = PhoneNumberField(blank=True)
    
    #Allergy tagging field comes here
    # allergys = 
    fachschaft = models.ForeignKey('Fachschaft', on_delete=models.CASCADE,)
    
    is_konrat   = models.BooleanField(default=False)
    is_vorstand = models.BooleanField(default=False)
    

class Event(models.Model):
    name       = models.CharField(max_length=240, blank=True)
    name_short = models.CharField(max_length=10, blank=True)
    iteration  = models.IntegerField()
    location   = models.CharField(max_length=240, blank=True)
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    date_end   = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)


class Allergy(models.Model):
    name = models.CharField(max_length=240, blank=True)
    


    