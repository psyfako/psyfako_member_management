from django.conf.urls import url
from datetime import datetime

from . import views

app_name = 'timetable'

urlpatterns = [
    url(r'^$', views.index, {'year': datetime.today().year, 'month': datetime.today().month, 'day': datetime.today().day}, name='index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.index, name='index'),
    url(r'^(?P<slot_id>[0-9]+)/$', views.detail, name='detail'),
]
