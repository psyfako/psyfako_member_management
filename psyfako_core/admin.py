from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Member)
admin.site.register(Fachschaft)
admin.site.register(Event)
admin.site.register(Allergy)