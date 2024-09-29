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
from .models import DiscussionPost, DiscussionComment,Registration
from .forms import DiscussionPostForm, DiscussionCommentForm
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

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

def summer(request):
    return render(request, 'summer.html')

def winter(request):
    return render(request, 'winter.html')

def elder(request):
    return render(request, 'elder.html')

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

def course_Analysis_Registration(request):
    return render(request, 'course_Analysis_Registration.html')

'''
def course_Registration(request):
    return render(request, 'course_Registration.html')
'''

def course_Analysis(request):
    return render(request, 'course_Analysis.html')

def member_center(request):
    return render(request, 'member_center.html')
#----------------------------------------------------------
# app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, MemberCenterForm
from django.contrib import messages
from django.http import JsonResponse

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

def community(request):
    posts = DiscussionPost.objects.all().order_by('-created_at')
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = DiscussionPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('community')
        else:
            return redirect('login')
    else:
        form = DiscussionPostForm() if request.user.is_authenticated else None
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

""""
class CourseRegistrationView(View):
    def get(self, request):
        return render(request, 'course_Registration.html')  # 确保有一个与前端代码匹配的模板

    def post(self, request):
        # 获取表单数据
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        grade = request.POST.get('grade')
        motivation = request.POST.getlist('motivation')
        techniques = request.POST.getlist('techniques')
        coach_gender = request.POST.get('coachGender')
        coach_traits = request.POST.getlist('coachTraits')
        course_type = request.POST.getlist('courseType')
        sub_course_type = request.POST.getlist('subCourseType')

        # 保存数据到数据库
        reservation = Reservation(
            name=name,
            gender=gender,
            phone=phone,
            email=email,
            grade=grade,
            motivation=motivation,
            techniques=techniques,
            coach_gender=coach_gender,
            coach_traits=coach_traits,
            course_type=course_type,
            sub_course_type=sub_course_type
        )
        reservation.save()

        return redirect('success')  # 这里可以跳转到成功页面或其他页面
        """


             
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

COURSE_PRICES = {
    '兒童初階班(每週二14:00 - 15:30)': 4000,
    '兒童初階班(每週二15:30 - 17:00)': 4000,
    '成人初階班(每週一14:00 - 16:00)': 4000,
    '成人初階班(每週一16:00 - 18:00)': 4000,
    '一般競技班(每週二14:00 - 16:00)': 4000,
    '一般競技班(每週四16:00 - 18:00)': 4000,
    '進階競技班(每週四14:00 - 16:00)': 4000,
    '進階競技班(每週四16:00 - 18:00)': 4000,
    '基礎擊打班(每週五19:00 - 22:00)': 350,
    '基礎擊打班(每週六19:00 - 22:00)': 350,
    '進階擊打班(每週五19:00 - 22:00)': 350,
    '進階擊打班(每週六19:00 - 22:00)': 350,
    '個別班': 0  
}

@csrf_protect
def course_Registration(request):
    if request.method == 'POST':
        selected_courses = request.POST.getlist('subCourseType') 
        course_type = request.POST.getlist('courseType')
        total_cost = 0

        for course in selected_courses:
            total_cost += COURSE_PRICES.get(course, 0)

        if '個別班' in course_type:
            total_cost += COURSE_PRICES.get('個別班', 0)

        return render(request, 'course_result.html', {'total_cost': total_cost, 'selected_courses': selected_courses})

    return render(request, 'course_Registration.html')


#編輯評論
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(DiscussionPost, id=post_id, author=request.user)
    
    if request.method == 'POST':
        form = DiscussionPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community')
    else:
        form = DiscussionPostForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': form, 'post': post})

#刪除評論
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(DiscussionPost, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('community')  
    
    return render(request, 'confirm_delete.html', {'post': post})

# 定義老師屬性
teachers = [
    {"name": "a", "gender": "男生", "skills": ["發球與接發球", "單打四角拉吊"], "traits": ["有經驗", "理論基礎"]},
    {"name": "b", "gender": "女生", "skills": ["雙打後場組織進攻", "發球與接發球"], "traits": ["有技術", "專業"]},
    {"name": "c", "gender": "男生", "skills": ["單打四角拉吊", "其他"], "traits": ["有經驗", "專業", "嚴厲"]},
    {"name": "d", "gender": "男生", "skills": ["發球與接發球", "雙打後場組織進攻"], "traits": ["多元", "有技術"]},
    {"name": "e", "gender": "男生", "skills": ["單打四角拉吊", "發球與接發球"], "traits": ["有技術", "理論基礎", "專業"]},
    {"name": "f", "gender": "女生", "skills": ["發球與接發球", "單打四角拉吊"], "traits": ["有經驗", "多元"]},
    {"name": "g", "gender": "女生", "skills": ["雙打後場組織進攻", "其他"], "traits": ["專業", "嚴厲"]}
]

# 匹配度計算函數
def calculate_match(teacher, preferences):
    score = 0
    
    # 嚴格匹配性別，如果指定了性別且不符合，直接返回0分
    if preferences["gender"] != "不指定" and teacher["gender"] != preferences["gender"]:
        return 0
    
    # 比較技術特長
    for skill in preferences["skills"]:
        if skill in teacher["skills"]:
            score += 2  # 技術匹配度給較高分
    
    # 比較教練特質
    for trait in preferences["traits"]:
        if trait in teacher["traits"]:
            score += 1
    
    return score

# 表單提交處理
@csrf_protect
def recommend_teacher(request):
    if request.method == 'POST':
        # 提取用戶提交的表單資料
        user_preferences = {
            "gender": request.POST.get("coachGender", "不指定"),  # 需要的教練性別
            "skills": request.POST.getlist("techniques"),  # 技術選擇 (可能多選)
            "traits": request.POST.getlist("coachTraits")  # 教練特質 (可能多選)
        }
        
        # 計算每位老師的匹配度
        teacher_scores = []
        for teacher in teachers:
            match_score = calculate_match(teacher, user_preferences)
            teacher_scores.append((teacher["name"], match_score))
        
        # 根據匹配度進行排序
        sorted_teachers = sorted(teacher_scores, key=lambda x: x[1], reverse=True)

        # 返回推薦結果
        recommended_teachers = [teacher for teacher, score in sorted_teachers if score > 0]

        # 渲染推薦結果
        return render(request, 'recommend_result.html', {'recommended_teachers': recommended_teachers})
    
    # 如果是 GET 請求，重定向到 course_Analysis_Registration.html
    return redirect('course_Analysis_Registration')
