from django.db import models

from psyfako_core.models import Member
from rooms.models import Room


class Slot(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=3, default='')
    start_time = models.DateTimeField('Start Time') 
    end_time = models.DateTimeField('End Time')
    
    def __str__(self):
        return self.name
                 
group_choices = ("Diskussion","Positionspapier")

class Workgroup(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default = '')
    group_type_choices = (
        ('O', 'Offen'),    
        ('A', 'Austausch'),
        ('W', 'Arbeit'),
        ('P', 'Positionspapier'),
    )
    group_type = models.CharField(max_length=1, choices=group_type_choices)
    moderation = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="moderation")
    protocol = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, related_name="protocol")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return self.title