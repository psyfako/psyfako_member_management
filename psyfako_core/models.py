from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Fachschaft(models.Model):
    university_name = models.CharField(max_length=240, blank=True)
    university_type = models.CharField(max_length=3, blank=True)
    city = models.CharField(max_length=240, blank=True)
    mail = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.university_type + " " +self.city
    

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=240, blank=False) # actualy I dont give a crap how people want to be called therfore in field 
    nickname = models.CharField(max_length=240, blank=True)
    
    # extendet user stats
    address_street       = models.CharField(max_length=240, blank=True)
    address_streetnumber = models.IntegerField(blank=True)
    address_city         = models.CharField(max_length=240, blank=True)
    address_citycode     = models.IntegerField(blank=True)
    
    mobilephone = PhoneNumberField(blank=True)
    
    #Allergy tagging field comes here
    # allergys = 
    fachschaft = models.ForeignKey('Fachschaft', on_delete=models.CASCADE, blank=True)
    
    is_konrat   = models.BooleanField(default=False)
    is_vorstand = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nickname + " (" +self.fachschaft.university_type + " " + self.fachschaft.city + ")"
    

class Event(models.Model):
    name       = models.CharField(max_length=240, blank=True)
    name_short = models.CharField(max_length=10, blank=True)
    iteration  = models.IntegerField()
    location   = models.CharField(max_length=240, blank=True)
    date_start = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    date_end   = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)


class Allergy(models.Model):
    name = models.CharField(max_length=240, blank=True)
    


    