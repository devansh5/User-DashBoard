from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


#custom form where we can add our own field


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    class meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name', 
            'username',
            'password1',
            'password2')
            
    
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )
class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)