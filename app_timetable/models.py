from django.db import models

class Slot(models.model):
    name = models.CharField(max_length=100, blank=True)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    class Meta:
        abstract=True
        
    
class OpenSpaceSlot(Slot):
    
