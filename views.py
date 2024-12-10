from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
#from tutor.models import Table
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def indexpage(request):
    return render(request,'index.html')

def signup_page(request):
    return render(request,'signup.html')

def logoutpage(request):
    logout(request)
    data=request.user
    return render(request,'index.html',{'data':False })

def loginpage(request):
    return render(request,'login.html')

def createuser(request):
    if request.method == 'POST':
        user = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        phone = request.POST.get('phone')

        if password != repassword:
            messages.error(request, "Passwords do not match.")
            return HttpResponseRedirect('/signup/')

        if User.objects.filter(username=user).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return HttpResponseRedirect('/signup/')
        # Create the user
        new_user = User.objects.create_user(username=user, password=password,email=email,id=phone)

        #Adding data to Profile

        data=request.user
        return render(request,'index.html',{'data':data})

def usercheck(request):
    if request.method == 'POST':
        user=request.POST.get('username')
        password=request.POST.get('password')
        x=authenticate(request,username=user,password=password)
        if x:
            login(request,x)
            data=request.user
            return render(request,'index.html',{'data':data})
        messages.info(request, 'invalid username or password' )
        return HttpResponseRedirect('/login/')#path
    if request.user:
        data=request.user
        return render(request,'index.html',{'data':data})
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def profilepage(request):
    current_user = request.user
    data = User.objects.filter(username=current_user.username).values()
    return render(request, 'profile.html',{'data':data})

def search(request):
    if request.method=='POST':
        search=request.POST.get('search')
        data = User.objects.filter(username__icontains=search)
        return render(request,'search.html',{'data':data})
    return render(request,'index.html')

def searchpage(request):
    return render(request,'search.html')
