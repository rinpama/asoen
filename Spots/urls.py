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
    path('createspotdetail', CreateSpotDetail, name='createspotdetail'),
    path('createcompanydetail', CreateCompanyDetail, name='createcompanydetail'),
path('createdetailcompany/<int:number>', CreateDetailCompany, name='createdetailcompany'),#nameを元にdetailCreate
path('createdetailaspot/<int:number>', CreateDetailAspot, name='createdetailapost'),#nameを元にdetailCreate

    path('logsouenlist',logSoenList,name='logsoenlist'),
path('loggenelist',logGeneList,name='loggenelist'),
path('logkyouryokulist',logKyouryokuList,name='logkyouryokulist'),
path('logaspotlist',logAspotList,name='logaspotlist'),
path('logcompanydetail/<int:number>', LogCompanyDetail, name='logcompanydetail'),
path('logaspotdetail/<int:number>', LogAspotDetail, name='logaspotdetail'),
]
