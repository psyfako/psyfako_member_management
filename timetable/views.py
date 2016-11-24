from django.shortcuts import get_object_or_404, render


from .models import Slot

def index(request):
    slot_list = Slot.objects.order_by('start_time')[:5]
    context = {
        'slot_list': slot_list,
    }
    return render(request, 'timetable/index.html', context)
    
def detail(request, slot_id):
    slot = get_object_or_404(Slot, pk=slot_id)
    return render(request, 'timetable/detail.html', {'slot': slot})

