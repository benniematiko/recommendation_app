from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 



class UsersInputForm(forms.Form):
    houseHold_Number = forms.IntegerField()
    Residence_Country = forms.CharField(max_length=65)
    housing_Size = forms.IntegerField()
    housing_Type = forms.CharField(max_length=65)
    daily_Electricity_Consumption = forms.IntegerField()
    energy_Source = forms.CharField(max_length=65)