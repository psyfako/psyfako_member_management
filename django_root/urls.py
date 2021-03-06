"""psyfako_member_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include

from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #url(r'^', include('dashboard.urls')),
    url(r'^', include('timetable.urls')),
 
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', include('allauth.urls')),

    url(r'^rooms/', include('rooms.urls')),
    url(r'^time/', include('timetable.urls')),
    url(r'^messages/', include('conmessages.urls')),
    #url(r'^main/', include('psyfako_core.urls')),
    
    # bonus
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^dash/', include('dashboard.urls')),
]

'''
    TODO enable favicon
    http://staticfiles.productiondjango.com/blog/failproof-favicons/
'''