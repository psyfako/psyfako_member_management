from django.shortcuts import render

from .models import Message

def index(request):
    conmsg_list = Message.objects.all().order_by('-time_sent')
    context = { 'conmsg_list' : conmsg_list }
    return render(request, 'conmessages/index.html', context)