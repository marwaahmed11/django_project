from django.urls import path 
from . import views 

urlpatterns = [
   
    path('showFund/<id>' , views.fundProject , name ="showFund"),
    path('showAllProjects/' , views.showAllProjects , name ="showAllProjects"),
    path('showUserProjects/' , views.showUserProjects , name ="showUserProjects"),
    path('createProject/' , views.createProject, name ="createProject"),
    path('showProject/<id>' , views.showProjectWithid , name ="showProject"),
    path('deleteProject/<id>' , views.deleteProjectWithid , name ="deleteProject"),
    path('updateProject/<id>' , views.updateProjectWithid , name ="updateProject"),
    path('Login/',views.LogUserIn,name="LoginForm"),
    path('Signup/',views.CreateUser,name="SignupForm"),
    path('Logout/',views.LogUserOut,name="Logout"),

]
