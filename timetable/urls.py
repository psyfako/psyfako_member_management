from django.conf.urls import url

from . import views

app_name = 'timetable'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slot_id>[0-9]+)/$', views.detail, name='detail'),
]
