from django.db import models

# Create your models here.
class studentstable(models.Model):
    Name= models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    Regno= models.IntegerField()
    EmailID= models.EmailField()
    Address= models.CharField(max_length=100)
    
    class Meta :
        db_table='data'
    
    
class studentmark(models.Model):
    Name= models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    Regno= models.IntegerField()
    Subject=models.CharField(max_length=250)
    Mark= models.IntegerField()
    Grade=models.CharField(max_length=100)   
    
    
    class Meta :
        db_table='mark'
     
    