from django.shortcuts import get_object_or_404, render
from datetime import datetime


from .models import Slot

def index(request, year, month, day):
    slot_list = Slot.objects.filter(start_time__year=str(year), start_time__month=str(month), start_time__day=str(day)).order_by('start_time')
    weekday = datetime(int(year), int(month), int(day)).weekday()
    if(weekday == 0):
        weekday = "Montag"
    elif(weekday == 1):
        weekday = "Dienstag"
    elif(weekday == 2):
        weekday = "Mittwoch"
    elif(weekday == 3):
        weekday = "Donnerstag"
    elif(weekday == 4):
        weekday = "Freitag"
    elif(weekday == 5):
        weekday = "Samstag"
    else:
        weekday = "Sonntag"
    
    day_before = int(day) - 1
    day_after= int(day) +1
    
    context = {
        'year': year,
        'month': month,
        'day': day,
        'day_before': day_before,
        'day_after': day_after,
        'weekday': weekday,
        'slot_list': slot_list,
    }
    return render(request, 'timetable/index.html', context)
    
def detail(request, slot_id):
    slot = get_object_or_404(Slot, pk=slot_id)
    return render(request, 'timetable/detail.html', {'slot': slot})

