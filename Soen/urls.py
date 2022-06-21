from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'Soen'
urlpatterns = [
    path('', SoenTop.as_view(), name='soentop'),
    path('soenmember', SoenMember.as_view(), name='soenmember'),
    path('shokukatamember', ShokukataMember.as_view(), name='shokukatamember'),
    path('uncategory', Uncategory.as_view(), name='uncategory'),

    path('soenmemberDetail/<int:number>', soenmemberDetail, name='soenmemberDetail'),
    path('health/<int:number>', soenmemberHealth, name='health'),
    path('vehicle/<int:number>', soenmemberVehicle, name='vehicle'),
    path('insurance/<int:number>', soenmemberInsurance, name='insurance'),
    path('skill/<int:number>', soenmemberEducationSkillLicence, name='educationskilllicence'),

    path('membercreate', CreateMember.as_view(), name='createmember'),
    path('memberedetailcreate/<int:number>', CreateDetailMember, name='createdetailmember'),
    path('createhealth/<int:number>', CreateHealth, name='createhealth'),
    path('createinsurance/<int:number>', CreateInsurance, name='createinsurance'),
    path('createeducationskilllicence/<int:number>', CreateEducationSkillLicence, name='createeducationskilllicence'),
path('createspecialeducation/<int:number>', CreateSpecialEducation, name='createspecialeducation'),
path('createskill/<int:number>', CreateSkill, name='createskill'),
path('createlicence/<int:number>', CreateLicence, name='createlicence'),
    path('createvehicle', CreateVehicle, name='createvehicle'),

    path('loginmemberlist', LoginMemberList, name='loginmemberlist'),
    path('loginshokukatalist', LoginShokukataList, name='loginshokukatalist'),
    path('loginuncategorylist', LoginUncategoryList, name='loginuncategorylist'),
path('loginvehiclelist', LoginVehicleList, name='loginvehiclelist'),

    path('logdetailmember/<int:number>', LoginDetailMember, name='logindetailmember'),
    path('logdetailhealth/<int:number>', LoginDetailHealth, name='logindetailhealth'),
    path('logdetailskill/<int:number>', LoginDetailSkill, name='logindetailskill'),
    path('logdetailvehicle/<int:number>', LoginDetailVehicle, name='logindetailvehicle'),
    path('logdetailinsurance/<int:number>', LoginDetailInsurance, name='logindetailinsurance'),

    path('updatemember/<int:number>', UpdateMemberView, name='updatemember'),
    path('updatehealth/<int:number>', UpdateHealthView, name='updatehealth'),
    path('updateskill/<int:number>', UpdateSkillView, name='updateskill'),
path('updatespecialeducationonly/<int:number>', UpdateSpecialEducationOnly, name='updatespecialeducationonly'),
path('updateskillonly/<int:number>', UpdateSkillOnly, name='updateskillonly'),
path('updatelicenceonly/<int:number>', UpdateLicenceOnly, name='updatelicenceonly'),

    path('updatevehicle/<int:number>', UpdateVehicleView, name='updatevehicle'),
    path('updateinsurance/<int:number>', UpdateInsuranceView, name='updateinsurance'),

    path('deletemember/<int:pk>/', SoenMemberDeleteView.as_view(), name='deletemember'),

]
