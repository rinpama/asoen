from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'Soen'
urlpatterns = [
    path('', SoenTop.as_view(), name='soentop'),
    path('soenmember', SoenMember.as_view(), name='soenmember'),
    path('shokukatamember', ShokukataMember.as_view(), name='shokukatamember'),
    path('uncategory', Uncategory.as_view(), name='uncategory'),

    path('soenmemberDetail/<int:pk>', soenmemberDetail.as_view(), name='soenmemberDetail'),
    path('health/<int:pk>', soenmemberHealth.as_view(), name='health'),
    path('vehicle/<int:pk>', soenmemberVehicle.as_view(), name='vehicle'),
    path('insurance/<int:pk>', soenmemberInsurance.as_view(), name='insurance'),
    path('skill/<int:pk>', soenmemberEducationSkillLicence.as_view(), name='educationskilllicence'),

    path('membercreate', CreateMember.as_view(), name='createmember'),

    # path('creatememberdetail', CreateMemberDetail.as_view(), name='creatememberdetail'),
    # path('creathealth', CreateHealth.as_view(), name='createhealth'),
    # path('createvehicle', CreateVehicle.as_view(), name='createvehicle'),

    path('loginmemberlist', LoginMemberList, name='loginmemberlist'),
    path('loginshokukatalist', LoginShokukataList, name='loginshokukatalist'),
    path('loginuncategorylist', LoginUncategoryList, name='loginuncategorylist'),

    path('detailmember/<int:number>', DetailMember, name='detailmember'),
    path('updatemember/<int:number>', UpdateMemberView, name='updatemember'),
    path('deletemember/<int:pk>/', SoenMemberDeleteView.as_view(), name='deletemember'),


]
