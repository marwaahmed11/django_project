from django import forms
from .models import Project, Funded_project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project 
        fields = '__all__' 
        exclude = ['user','current_situation'] 
        
class FundedForm(forms.ModelForm):
    class Meta:
        model = Funded_project 
        fields = '__all__' 

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']
