from django.db import models
from django.conf.urls import url
from . import views

app_name = 'user_profile'
urlpatterns = [
       url(r'^$', views.index, name='index')
]
