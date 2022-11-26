from email import message
import email
from queue import Empty
from django.shortcuts import render,redirect
from .models import studentmark
from .forms import mystudentstable
from .forms import mystudentmark
from .forms import studentmark
from .forms import CreateUserForm
from django.contrib import messages
from .models import studentstable

from django.contrib.auth.models import User 

# Create your views here.
def fpage (request):
    return render(request,"fpage.html")
def loginpage(request):
    return render(request,"loginpage.html")

def Login(request):
    return render(request,"login.html")

def Register(request):
    if request.method=="POST":
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1==password2:
            
            user=User.objects.create_user(username=name,email=email,password=password1)
            
            
            user.save()
            messages.success(request,'Successfully Registered')
            return redirect('Login')
        else:
            messages.warning(request,'Password missmatch....!')
            return redirect('Register')    
    else:
        form=CreateUserForm()
        return render(request,"Registration.html",{'form':form})


    
def profile(request,):
  
           
    return render(request,"profile.html")


def home(request):
    data= studentstable.objects.all()
    if (data !=''):
        return render(request,"home.html",{'data':data })
    else:
        return render(request,"home.html")

def insert(request):
    if request.method=='POST':
        form = mystudentstable(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Student has been added successfully")
                return redirect("Home")
            except:
                pass 
    else:          
        form= mystudentstable()
        return render(request,"insert.html",{'form':form})    



#def login(request):
    #return render(request,"loginpage.html")



def studentlogin(request):
    return render(request,"studentlogin.html")

def studentsinfo(request):
    data= studentstable.objects.all()
    return render(request,"studentsinfo.html",{'data':data })
   

def studentsupdate(request):
    data= studentstable.objects.all()
    if (data !=''):
        return render(request,"studentsupdate.html",{'data':data })
    else:
        return render(request,"studentsupdate.html")
    
def update(request,id):
    data=studentstable.objects.get(id=id)
    if request.method=="POST":
           Name= request.POST['Name']
           Department= request.POST['Department']
           Regno= request.POST['Regno']
           EmailID= request.POST['EmailID']
           Address= request.POST['Address']
           
           
           data.Name=Name
           data.Department=Department
           data.Regno=Regno
           data.EmailID=EmailID
           data.Address=Address
           data.save()
           messages.success(request,"successfully Updated")
           return redirect("studentsupdate")
    return render(request,"update.html",{'data':data})
    
        
def admindashboard(request):
    return render(request,"admindashboard.html")   

def studentmarks(request):
    data= studentmark.objects.all()
    if (data !=''):
        return render(request,"studentmark.html",{'data':data })
    else:
        return render(request,"studentmark.html")
    
def insertmark(request):
    if request.method=='POST':
        form = mystudentmark(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Student has been added successfully")
                return redirect("studentmarks")
            except:
                pass 
    else:          
        form= mystudentmark()
        return render(request,"insertmark.html",{'form':form})       
    
    
def infomark(request):
    data= studentmark.objects.all()
    return render(request,"infomark.html",{'data':data })
       
def studentmarkupdate(request):
    data= studentmark.objects.all()
    if (data !=''):
        return render(request,"studentmarkupdate.html",{'data':data })
    else:
        return render(request,"studentmarkupdate.html")    
    
def updatemark(request,id):
    data=studentmark.objects.get(id=id)
    if request.method=="POST":
           Name= request.POST['Name']
           Department= request.POST['Department']
           Regno= request.POST['Regno']
           Subject= request.POST['Subject']
           Mark= request.POST['Mark']
           Grade= request.POST['Grade']
           
           
           data.Name=Name
           data.Department=Department
           data.Regno=Regno
           data.Subject= Subject
           data.Mark=Mark
           data.Grade= Grade
           data.save()
           messages.success(request,"Mark has been updated successfully ")
           return redirect("studentmarkupdate")
    return render(request,"updatemark.html",{'data':data})    


def mech(request):
    return render(request,"mech.html")

def IT(request):
    return render(request,"IT.html")

def CSE(request):
    return render(request,"CSE.html")

def EEE(request):
    return render(request,"EEE.html")

def ECE(request):
    return render(request,"ECE.html")

def civil(request):
    return render(request,"civil.html")

