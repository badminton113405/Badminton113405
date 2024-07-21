from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm as DjangoPasswordResetForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'nickname', 'gender', 'birth_date', 'phone', 'email', 'username', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '請輸入帳號'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '請輸入密碼'}))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'nickname', 'gender', 'birth_date', 'occupation', 'phone', 'email']

class PasswordResetForm(DjangoPasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': '請輸入您的Email'}))