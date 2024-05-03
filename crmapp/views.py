from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate
from crmapp.models import userdetails

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login1(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def add_details(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        address=request.POST['address']
        email=request.POST['email']
        number=request.POST['num'] 
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        cpswd=request.POST['cpswd']
        if pswd == cpswd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'This username already exists!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    email=email,
                    password=pswd
                )
                user.save()
                u=User.objects.get(id=user.id)
                reg=userdetails.objects.create(
                    address=address,
                    phone=number,
                    user=u
                )
                reg.save()
                messages.success(request, 'Profile created successfully!')
                return redirect('home')
        else:
            messages.info(request, 'Password doesnt match')
            return redirect('signup')
    return render(request, 'login.html') 


def adminlogin(request):
    if request.method == "POST":
        username=request.POST['uname']
        password=request.POST['pswd']  
        user=authenticate(username=username, password=password)  
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('adminhome')
            else:
                login(request, user)
                return redirect('user_home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login1')
    return render(request, 'login.html')

def logout1(request):
    auth.logout(request)
    return redirect('home')


def user_home(request):
    return render(request,'log.html')






