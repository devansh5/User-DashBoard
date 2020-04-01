from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=150)
    picture=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)




