#!python
# log/urls.py
from django.conf.urls import url

from manager import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profile/', views.updateUser, name='profile'),
    url(r'maintain/updaterequest/(?P<pk>\d+)', views.updateMaintenanceRequest, name='requestdetail'),
    url(r'^maintain/$', views.createMaintenanceRequest, name="maintenance"),
    url(r'^dashboard/$', views.dashboard, name="dashboard")
]
