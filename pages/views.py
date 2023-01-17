from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,CreateUserForm,FundedForm
from django.contrib.auth.models import User

def showAllProjects(request):
    return render(request,'pages/showAllProjects.html',{"projects":Project.objects.all().order_by('id')}) #=> return all elements
    #  return render(request,'pages/cars.html', {"car":Car.objects.get(name ="bmw")})  #=> get return only one element
    # return render(request,'pages/cars.html', {"cars":Car.objects.filter(name = "car2")})  #filterlazm andeha bloop 
    # cars = Car.objects.all().filter(price__exact='99')
    #  cars = Car.objects.all().filter(price__contains='99')
    #  cars = Car.objects.all().order_by('model').exclude(name="lancer")
    #  dic = {"cars":cars}
    #  return render(request,'pages/cars.html', dic)
 


@login_required(login_url='login')
def createProject(request):
    project = ProjectForm(request.POST, request.FILES)
    if project.is_valid():
        instance = project.save(commit=False) 
        instance.user = request.user
        instance.save()
        project.save() 
    else :
        print("not valid")
    return render(request,'pages/createProject.html',{"form":ProjectForm})

def fundProject (request,id):
    project= Project.objects.get(pk = id)
    val=FundedForm(request.POST)
    if val.is_valid():
       instance = val.save(commit=False) #msh bt7otha f table
       project.current_situation+=int(instance.value)  
       project.save()
       return redirect('showAllProjects')
    project = Project.objects.get(pk = id)
    return render(request,'pages/showFund.html',{"form" : val})

def showProjectWithid (request,id):
    project= Project.objects.get(pk = id)
    return render(request,'pages/projectDetails.html',{"project" : project})
  

def showUserProjects (request):
    project= Project.objects.filter(user=request.user.id).values()
    return render(request,'pages/showUserProjects.html',{"projects" : project})

@login_required(login_url='login')
def deleteProjectWithid  (request,id):
    project= Project.objects.get(pk = id)
    project.delete()
    projects = Project.objects.all().order_by('id')
    return render(request,'pages/showAllProjects.html',{"projects" : projects})

@login_required(login_url='login')
def  updateProjectWithid (request,id):
    project_id= Project.objects.get(pk = id)
    form = ProjectForm(request.POST or None,instance=project_id)
    if form.is_valid():
        form.save()
        return redirect('showAllProjects')
    else :
        print("not valid")
    return render(request,'pages/updateProject.html',{"project" : project_id,"form" : form})



def LogUserIn(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            #to be edited
            # return redirect('showAllProjects')
            return redirect('showUserProjects')
        else:
            messages.error(request,"Invalid  password.")
    else:
        messages.error(request,"Invalid username or password.")
    return render(request,'pages/Login.html')


def LogUserOut(request):
    logout(request)
    return redirect('LoginForm')


def CreateUser(request):
    SignedUser=CreateUserForm(request.POST)
    if SignedUser.is_valid():
         SignedUser.save()
         userName=SignedUser.cleaned_data.get('username')
         messages.success(request,"account has been created for"+userName)
         return redirect('LoginForm')
    SignedUser=CreateUserForm()
    return render(request,'pages/Signup.html',{"Form":SignedUser})

  