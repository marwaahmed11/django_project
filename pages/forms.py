from django import forms
from .models import Project,created_project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        fields = '__all__' # get all fields of car table 
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']

class CreatedProjectForm(forms.ModelForm):
    class Meta:
        model = created_project
        fields = '__all__' # get all fields of car table 

# class DonateForm(forms.ModelForm):
#     class Meta:
#         model = 
#         fields = '__all__' # get all fields of car table 