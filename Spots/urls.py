from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'Spots'
urlpatterns = [
    path('', SpotsTop.as_view(), name='spotstop'),
    path('spotlist', spotlist, name='spotlist'),
    path('generallist', generallist, name='generallist'),
    path('cooperatelist', cooperatelist, name='cooperatelist'),
    path('soenlist', soenlist, name='soenlist'),
    path('spotcreate', SpotCreate.as_view(), name='spotcreate'),
    path('companycreate', CompanyCreate.as_view(), name='companycreate'),

]
