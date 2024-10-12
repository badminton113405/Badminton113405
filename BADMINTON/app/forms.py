from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, DiscussionPost, DiscussionComment
from django.forms.widgets import SelectDateWidget

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, 2024)))

    class Meta:
        model = User
        fields = ['username', 'full_name', 'gender', 'birth_date', 'nickname', 'phone', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birth_date': forms.SelectDateWidget(attrs={'class': 'dob'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, 2024)))

    class Meta:
        model = User
        fields = ['full_name', 'gender', 'birth_date', 'nickname', 'phone', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'profile-info-input'}),
            'gender': forms.Select(attrs={'class': 'profile-info-select'}),
            'birth_date': forms.SelectDateWidget(attrs={'class': 'dob'}),
            'nickname': forms.TextInput(attrs={'class': 'profile-info-input'}),
            'phone': forms.TextInput(attrs={'class': 'profile-info-input'}),
            'email': forms.EmailInput(attrs={'class': 'profile-info-input'}),
        }
     
class MemberCenterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'gender', 'birth_date', 'nickname', 'phone', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'gender': forms.Select(attrs={'disabled': 'disabled'}),
            'birth_date': forms.DateInput(attrs={'readonly': 'readonly'}),
            'nickname': forms.TextInput(attrs={'readonly': 'readonly'}),
            'phone': forms.TextInput(attrs={'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }

class DiscussionPostForm(forms.ModelForm):
    class Meta:
        model = DiscussionPost
        fields = ['content']

class DiscussionCommentForm(forms.ModelForm):
    class Meta:
        model = DiscussionComment
        fields = ['content']
