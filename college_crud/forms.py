
from django import forms
from .models import studentstable
from .models import studentmark
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User          

class mystudentstable(forms.ModelForm):
    class Meta:
        model= studentstable
        fields=["Name","Department","Regno","EmailID","Address"]
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=["username","email","password1","password2"]     
        
        
class mystudentmark(forms.ModelForm):
    class Meta:
        model= studentmark
        fields=["Name","Department","Regno","Subject","Mark","Grade"]           