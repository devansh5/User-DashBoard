from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms.widgets import RadioSelect



class Profile(models.Model):
    CHOICES=[('Male','Male'),
        ('Female','Female'),
        ('Other','Other')]
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=150)
    address1=models.CharField(max_length=250,default="")
    address2=models.CharField(max_length=250,default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    gender=models.CharField(max_length=11,choices=CHOICES,blank=True)
    pin=models.CharField(max_length=15,default="")
    country=models.CharField(max_length=50,default="")
    mobileno=models.CharField(max_length=12,default=0)





    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)




