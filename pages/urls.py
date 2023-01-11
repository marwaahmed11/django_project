from django.urls import path 
from . import views 

urlpatterns = [
    path('index/',views.pagesIndex ,name = 'pagesindex'), # => lma a3ml urls.py elso3'yra 
    path('about/',views.pagesAbout,name ="pagesabout"), # =>http://localhost:8000/pages/about
    # path('',views.pagesAbout),       # =>http://localhost:8000/pages/about
     path('index.html/',views.renderHtml,name ="pagesindexhtml"),
    path('about.html/',views.renderHtml2,name ="pagesabouthtml"),
    path('showAllProjects/' , views.showAllProjects , name ="showAllProjects"),
    # path('task1/' , views.task1 , name ="viewtask1"),
    path('createProject/' , views.createProject, name ="createProject"),
    path('showProject/<id>' , views.showProjectWithid , name ="showProject"),
    path('deleteProject/<id>' , views.deleteProjectWithid , name ="deleteProject"),
    path('updateProject/<id>' , views.updateProjectWithid , name ="updateProject"),
    path('Login/',views.LogUserIn,name="LoginForm"),
    path('Signup/',views.CreateUser,name="SignupForm"),
    path('Logout/',views.LogUserOut,name="Logout"),

]
