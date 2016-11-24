from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=5)
    adress = models.CharField(max_length=200)
    lat = models.CharField(max_length=200, blank=True)
    lng = models.CharField(max_length=200, blank=True)
    
    
    
    def __str__(self):
        return self.name
        
class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    floor = models.CharField(max_length=2)
    nr = models.CharField(max_length=4)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name + " (" +self.building.short_name +"/" + self.floor + "." + self.nr +")" + " - " + str(self.capacity) +" Personen" 
    
