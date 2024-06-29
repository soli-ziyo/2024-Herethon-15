from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout 

# Create your views here.

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            li_email=form.cleaned_data.get('username')
            li_pw=form.cleaned_data.get('password')
            user=authenticate(request=request, username=li_email, password=li_pw)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                return render(request, 'login_fail.html',{'form':form})
        
    else:
        form=AuthenticationForm()
        return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')