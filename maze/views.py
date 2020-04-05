from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import CreateUserForm,EditProfileForm,ProfileUpdate
from django.contrib.auth.decorators import login_required
from .models import *
import json

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode





def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.POST.get('act') == 'post':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        data = {'username':username,'email':email,'password1':password1,'password2':password2}
        form = CreateUserForm(data=data)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return HttpResponse(json.dumps({"message":"Success"}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message":form.errors}),content_type="application/json")
    else:
        form=CreateUserForm()
    return HttpResponse(json.dumps({"message":"Denied"}),content_type="application/json")


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.POST.get('action') == 'post':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponse(json.dumps({"message":"Success"}),content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message":"inactive"}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "invalid"}),content_type="application/json")
        return HttpResponse(json.dumps({"message":"denied"}),content_type="application/json")

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return render(request,'maze/index.html')
  

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


