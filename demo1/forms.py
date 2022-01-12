from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from demo1.models import registermodel
from django.contrib.auth.hashers import make_password


class NEWUSER(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','password2','email']
        
        
class registerform(forms.ModelForm):
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=registermodel
        fields=['username','first_name','last_name','email','phone','gender','age','password']
    def save(self,commit=True):
        user=super(registerform,self).save(commit=False)
        user.password=make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        