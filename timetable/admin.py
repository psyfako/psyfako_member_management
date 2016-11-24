from django.contrib import admin

from .models import Slot
from .models import Workgroup

admin.site.register(Slot)
admin.site.register(Workgroup)

