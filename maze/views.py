from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import CreateUserForm,EditProfileForm,ProfileUpdate
from django.contrib.auth.decorators import login_required
from .models import *





def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
            else:
                messages.info(request,'Password is too short ,min - 8 char')

        context = {'form':form}
        return render(request,'maze/register.html',context)


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = { }
        return render(request,'maze/login.html',context)

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('/')
  

def index(request):
    return render(request,'maze/index.html')

@login_required(login_url='login')
def view_profile(request):
    args={'user':request.user}
    return render(request,'maze/profile.html',args)

@login_required(login_url='login')
def edit_profile(request):

    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return HttpResponse("invalid user_profile!")

    if request.method == 'POST':
        form = EditProfileForm(request.POST ,instance=request.user)
        profile_form=ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('profile')
    
    else:
        form = EditProfileForm(instance=request.user)
        profile_form=ProfileUpdate(instance=request.user.profile)
        args = {'form':form,'profile_form':profile_form}
        return render(request,'maze/edit.html',args)

@login_required(login_url='login')
def password_change(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Your Password was successfully updated! ')
            return redirect('profile')
        else:
            return redirect('changepassword')
    else:
        form=PasswordChangeForm(request.user)

        args={'form':form}
        return render(request,'maze/passwordchange.html',args)


