from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    options= [("Art","Art"),("Design","Design"),("Food","Food"),("Games","Games")] #=>year w7da htzhrli w w7da htt7t fe database
    name = models.CharField(max_length=50 ,  verbose_name="Project Title") #=>verbose 3shan yzhr f admin page asmha title
    current_situation = models.IntegerField(default=0,null=True)
    image = models.ImageField(blank= True,upload_to='photos/%y/%m/%d')
    target=models.DecimalField(max_digits=10, decimal_places=3,null=True)
    description = models.CharField(max_length=10000,null=True)#=>lw md5lsh input htkon null
    category = models.CharField(default="default", choices=options , max_length=50) #=> option for models
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    user = models.ForeignKey(User, default=None,null=True, on_delete=models.CASCADE)

    def __str__(self):  #=> must return a string 
       return self.name  #=> 3shan t5li project tzhr b2smha msh id
    #    return str(self.price)
    class Meta:
        ordering = ['name'] #=> order ascending 
        verbose_name = "Project" #=> asm class f admin page


class Funded_project(models.Model):
  value = models.IntegerField()