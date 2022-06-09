from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logintop/', views.LoginTop.as_view(), name='logintop'),
    path('logout/', views.Logout.as_view(), name='logout'),

]
