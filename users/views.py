from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    return HttpResponse('hey')
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('hey')  
        else:
           
            return render(request, 'authentication/signin.html', {'error_message': 'Invalid credentials'})
    return render(request, 'authentication/signin.html')   
    return render(request,'authentication/signup.html')