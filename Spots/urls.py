from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'Spots'
urlpatterns = [
    path('', SpotsTop.as_view(), name='spotstop'),
    path('spotcreate', SpotCreate.as_view(), name='spotcreate'),

]
