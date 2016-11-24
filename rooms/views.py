from django.shortcuts import get_object_or_404, render


from .models import Room

    
def detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'rooms/detail.html', {'room': room})