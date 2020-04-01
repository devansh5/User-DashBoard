from . import views

from django.urls import path


urlpatterns=[
    path('',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('profile/',views.view_profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('profile/passwordchange/',views.password_change,name='password_change'),
]