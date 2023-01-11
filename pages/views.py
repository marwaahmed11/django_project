from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,created_project
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, CreatedProjectForm ,CreateUserForm
from django.contrib.auth.models import User

# Create your views here.
def pagesIndex(request):
    return HttpResponse ("Hello from pages index")

def pagesAbout(request):
    return HttpResponse ("Hello from pages about")

def renderHtml(request):
    # dic ={"user":"marwa","name":"ahmed @@@@ ali","salary":100000}
    newdic =[{"user":"ahmed","salary":100000},{"user":"omar","salary":200000}]
    dic = {"users" : newdic}
    return render(request,'pages/index.html',dic)

def renderHtml2(request):
    dic = {"user" :"hello"}
    return render(request,'pages/about.html',dic)


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
        project.save()
        user_id= request.user.id
        obj= Project.objects.latest('id')
        project_id = obj.id # get row
        result =  created_project(user_id=user_id,project_id=project_id)
        result.save()
    
    else :
        print("not valid")
    return render(request,'pages/createProject.html',{"form":ProjectForm})


def showProjectWithid (request,id):
    project= Project.objects.get(pk = id)
    return render(request,'pages/projectDetails.html',{"project" : project})
    # return HttpResponse(project)

@login_required(login_url='login')
def deleteProjectWithid  (request,id):
    project= Project.objects.get(pk = id)
    project.delete()
    projects = Project.objects.all().order_by('id')
    return render(request,'pages/showAllProjects.html',{"projects" : projects})
    # return HttpResponse(project)

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

@login_required(login_url='login')
def donate(request):
    project = ProjectForm(request.POST, request.FILES)
    if project.is_valid():
        project.save()
        user_id= request.user.id
        obj= Project.objects.latest('id')
        project_id = obj.id # get row
        result =  created_project(user_id=user_id,project_id=project_id)
        result.save()
    
    else :
        print("not valid")
    return render(request,'pages/createProject.html',{"form":ProjectForm})



def LogUserIn(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            #to be edited
            return redirect('showAllProjects')
        else:
            messages.error(request,"Invalid  password.")
    else:
        messages.error(request,"Invalid username or password.")
    return render(request,'pages/Login.html')

# def CreateUser(request):
#     SignedUser=user_registerForms(request.POST,request.FILES)
#     if SignedUser.is_valid():
#          SignedUser.save()
#     return render(request,'User/Signup.html',{"Form":SignedUser})

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

  