from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

from .models import user
from django.contrib import messages


def learn(request):
    return render(request,"index.html")
def register(request):
    return render(request,"register.html")
def admi (request):
    return render(request,"admin.html")
def img(request):
    return render(request,"image.jpeg")

def user_details(request):
    return render(request,"user_details.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        mobile = request.POST['mobile']
        proof=request.FILES['proof']
        if password == confirmpassword:
            if user.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif user.objects.filter(username = username).exists():
                messages.info(request,'username Already used')
                return redirect('register')
            else:
                users = user(username = username,email=email,password = password,mobile=mobile,proof=proof)
                users.save()
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('register')
    else:
        return render(request,'register.html')
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate( request,username=username, password=password)
        
        if user is not None:
            # Login successful
            login(request, user)
            return redirect('user_details')  # Redirect to a success page
        else:
            # Login unsuccessful
            messages.error(request, 'Invalid username or password')
            return render(request, 'index.html')  # Render login page again with error message
    else:
        # If GET request, render the login page
        return render(request, 'index.html')
