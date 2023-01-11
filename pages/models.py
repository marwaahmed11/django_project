from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    options= [("Art","Art"),("Design","Design"),("Food","Food"),("Games","Games")] #=>year w7da htzhrli w w7da htt7t fe database
    name = models.CharField(max_length=50 ,  verbose_name="Project Title") #=>verbose 3shan yzhr f admin page asmha title
    current_situation = models.DecimalField(max_digits=7, decimal_places=2,null=True)
    image = models.ImageField(blank= True,upload_to='photos/%y/%m/%d')
    target=models.DecimalField(max_digits=10, decimal_places=3,null=True)
    description = models.CharField(max_length=10000,null=True)#=>lw md5lsh input htkon null
    category = models.CharField(default="default", choices=options , max_length=50) #=> option for models
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
   


    def __str__(self):  #=> must return a string 
       return self.name  #=> 3shan t5li car tzhr b2smha msh id
    #    return str(self.price)
    class Meta:
        ordering = ['name'] #=> order ascending 
        # ordering = ['-name'] #=> order descending 
        verbose_name = "Project" #=> asm class f admin page



# class Employee(models.Model):
#     name = models.CharField(max_length = 50 )
#     age = models.IntegerField()
#     # relation = models.OneToOneField(Car , on_delete = models.PROTECT, null=True,blank=True) #=> lw ms7t employee, car mwgoda 
#     # relation = models.OneToOneField(Car , on_delete = models.CASCADE, null=True,blank=True) #=> lw ms7t employee, car mwgoda 
#     cars = models.ManyToManyField(Project)
#     def __str__(self):
#         return self.name  

class created_project(models.Model):
  user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
 

class Funded_project(models.Model):
  user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
  value = models.IntegerField()