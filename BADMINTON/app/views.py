from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.decorators import login_required
from .models import DiscussionPost, DiscussionComment
from .forms import DiscussionPostForm, DiscussionCommentForm

def home(request):
    return render(request, 'home.html')

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

def community(request):
    return render(request, 'community.html')

def mall(request):
    return render(request, 'mall.html')

def shopingcar(request):
    return render(request, 'shopingcar.html')

def product01(request):
    return render(request, 'product01.html')

def product02(request):
    return render(request, 'product02.html')

def product03(request):
    return render(request, 'product03.html')

def product04(request):
    return render(request, 'product04.html')

def product05(request):
    return render(request, 'product05.html')

def product06(request):
    return render(request, 'product06.html')

def product07(request):
    return render(request, 'product07.html')

def product08(request):
    return render(request, 'product08.html')
#----------------------------------------------------------
# app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, MemberCenterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '註冊成功！')
            return redirect('member_center')
        else:
            messages.error(request, '註冊失敗!!')
            print(form.errors)  
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '登入成功！')
                return redirect('member_center')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def member_center(request):
    user = request.user
    form = MemberCenterForm(instance=user)
    return render(request, 'member_center.html', {'form': form})

@login_required
def edit_member(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '編輯成功！')
            return redirect('member_center')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_member.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def member_redirect(request):
    if request.user.is_authenticated:
        return redirect('member_center')
    else:
        return redirect('login')
    


User = get_user_model()

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            reset_link = request.build_absolute_uri(
                f"/reset-password/{uid}/{token}/"
            )
            subject = 'Reset your password'
            message = render_to_string('reset_password_email.html', {
                'reset_link': reset_link,
                'user': user,
            })
            send_mail(subject, message, 'admin@example.com', [user.email])
            return render(request, 'forgot_password_done.html')
        except User.DoesNotExist:
            return render(request, 'forgot_password.html', {'error': 'Email not found'})
    return render(request, 'forgot_password.html')

def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, '重設成功!!')    
                return redirect('login')
            else:
                messages.error(request, '重設失敗!!')    
        else:
            form = SetPasswordForm(user)
        return render(request, 'reset_password.html', {'form': form})
    else:
        return render(request, 'reset_password_invalid.html')

@login_required
def community(request):
    posts = DiscussionPost.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = DiscussionPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community')
    else:
        form = DiscussionPostForm()
    return render(request, 'community.html', {'posts': posts, 'form': form})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(DiscussionPost, id=post_id)
    if request.method == 'POST':
        form = DiscussionCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('community')
    return redirect('community')