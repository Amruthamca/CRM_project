from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login1',views.login1,name='login1'),
    path('signup',views.signup,name='signup'),
    path('user_home',views.user_home,name='user_home'),
    path('add_details',views.add_details,name='add_details'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('logout1',views.logout1,name='logout1'),
    #path('archived',views.archived,name='archived')
   
    
]