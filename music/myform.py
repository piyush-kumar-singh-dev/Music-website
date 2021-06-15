from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class Register(forms.ModelForm):
    password=forms.CharField(min_length=8,widget=forms.PasswordInput)
    confirm_password=forms.CharField(min_length=8,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
    def clean(self):
        p=self.cleaned_data.get("password")
        p1=self.cleaned_data.get("confirm_password")
        super().clean()
        if p!=p1:
            raise ValidationError("password did not match")

class Loginpage(forms.Form):
    username=forms.CharField(max_length=40)
    password=forms.CharField(min_length=8,widget=forms.PasswordInput)
    def clean(self):
        u=self.cleaned_data.get('username')
        p = self.cleaned_data.get('password')
        if not (authenticate(username=u,password=p)):
            raise forms.ValidationError('invalid username or password ')
