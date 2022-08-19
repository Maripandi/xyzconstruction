#from fileinput import FileInput



from unicodedata import name
from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import *


class CustomUserForm(UserCreationForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username','name':'username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email','autocomplete':'off','name':'email'}))
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the first Name of user','name':'first_name'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the last Name of user','name':'last_name'}))
    password1=forms.Field(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter the New password','name':'password'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter the password again'}))


class EmployeeProfileForm(CustomUserForm):
    emp_phon=forms.CharField(label='Employee Phone Number',max_length=13,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the Emplyee Phone Number','name':'emp_phon'}))
    emp_address=forms.CharField(label='Employee Address', max_length=500,widget=forms.Textarea(attrs={'class':'form-control','rows':3,'name':'emp_address'}))
    profile_pic=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','name':'profile_pic'}))
    class Meta:
        model=Employee
        fields=(
                'username',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'emp_phon',
                'emp_address',
                'profile_pic'
                )

# class CustomUserForm2(UserCreationForm): 
#     username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username','name':'username'}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email','autocomplete':'off','name':'email'}))
#     first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the first Name of user','name':'first_name'}))
#     last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the last Name of user','name':'last_name'}))
#     password1=forms.Field(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter the New password','name':'password'}))
#     password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter the password again'}))



class AdminProfileForm(CustomUserForm):    #100 % working            
    admin_phon=forms.CharField(label='Admin Phone Number',max_length=13,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the Admin Phone Number','name':'admin_phon'}))
    admin_address=forms.CharField(label='Admin Address', max_length=500,widget=forms.Textarea(attrs={'class':'form-control','rows':3,'name':'admin_address'}))
    # profile_pic=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','name':'profile_pic'}))
 
    class Meta:
        model=Admin
        fields=(
                'username',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'admin_phon',
                'admin_address',
                # 'profile_pic'
                )
class ProfilePicUploadForm(forms.Form):
    profile_pic=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','name':'profile_pic'}))

class BlogPostForm(forms.Form): #not working
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title','name':'title'}))
    current_pic=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    old_pic=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    updates=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Enter the Points'}))

    class Meta:
        model=Blog
        fields=['title',
                'current_pic',
                'old_pic',
                'updates'
                ]
