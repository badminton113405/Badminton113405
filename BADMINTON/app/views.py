from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def community(request):
    comments = [
        {'text': '一起打球嗎', 'editing': False},
        {'text': '有人要一起上團課嗎', 'editing': False}
    ]
    return render(request, 'community.html', {'comments': comments})

def beginner(request):
    return render(request, 'beginner.html')

def competitive(request):
    return render(request, 'competitive.html')

def onetoone(request):
    return render(request, 'onetoone.html')

def zerodozen(request):
    return render(request, 'zerodozen.html')

def ZZT(request):
    return render(request, 'ZZT.html')

def HWH(request):
    return render(request, 'HWH.html')

def CYZ(request):
    return render(request, 'CYZ.html')

def ZBY(request):
    return render(request, 'ZBY.html')

def power_ball(request):
    return render(request, 'power_ball.html')

def left_right_ball(request):
    return render(request, 'left_right_ball.html')

def small_ball(request):
    return render(request, 'small_ball.html')
#----------------------------------------------------------

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, PasswordResetForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('member_center')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('member_center')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def member_center(request):
    return render(request, 'member_center.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('member_center')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password reset email has been sent.')
            return redirect('login')
    else:
        form = PasswordResetForm()
    return render(request, 'forgot_password.html', {'form': form})