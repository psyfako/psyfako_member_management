from django.contrib import admin

from .models import Message
from .models import Channel

admin.site.register(Message)
admin.site.register(Channel)