"""Collegeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from college_crud import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.loginpage,name="loginpage"),
    path('Login/', auth_views.LoginView.as_view(template_name='login.html'),name="Login"),
    path('Logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name="Logout"),
    path('Register/', views.Register,name="Register"),
    path('profile/',views.profile,name="Profile"),
    path('insert/',views.insert,name='Insert'),
    path('home/',views.home,name='Home'),
    path('admindashboard/',views.admindashboard),
    path('studentsupdate',views.studentsupdate,name='studentsupdate'),
    path('update/<int:id>',views.update,name="update"),
    path('studentmarks/',views.studentmarks,name='studentmarks'),
    path('insertmark/',views.insertmark,name='insertmark'),
    path('infomark/',views.infomark,name='infomark'),
    path('studentmarkupdate',views.studentmarkupdate,name='studentmarkupdate'),
    path('updatemark/<int:id>',views.updatemark,name="updatemark"),
    path('mech/',views.mech,name='mech'),
    path('IT/',views.IT,name='IT'),
    path('CSE/',views.CSE,name='CSE'),
    path('EEE/',views.EEE,name='EEE'),
    path('ECE/',views.ECE,name='ECE'),
    path('civil/',views.civil,name='civil'),
    
    
    
    
    
    
   
    
    
  
    
    
    
    
    
    
    path('studentsinfo',views.studentsinfo),
    
    path('home/',views.home,name='Home'),
    
    
    
    path('studentlogin/',views.studentlogin),
    
   
    
    
    
]
