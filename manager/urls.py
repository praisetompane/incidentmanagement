#!python
# log/urls.py
from django.conf.urls import url

from manager import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/updaterequest/(?P<pk>\d+)', views.updateMaintenance, name='requestdetail'),
    url(r'^updaterequest/(?P<pk>\d+)', views.updateMaintenance, name='requestdetail'),
    url(r'^maintain/', views.maintenance, name="maintenance")
]
