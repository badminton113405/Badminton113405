import json
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.decorators import login_required
from .models import DiscussionPost, Order, CourseRegistration,Product,  OrderItem,CourseType, Coach,CoachAvailability
from .forms import (
    DiscussionPostForm,
    DiscussionCommentForm,
    UserRegistrationForm,
    UserLoginForm,
    UserProfileForm,
    MemberCenterForm,
)
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages
from decimal import Decimal
from datetime import date, timedelta


def home(request):
    courses = CourseType.objects.all()
    coaches = Coach.objects.all()
    return render(request, 'home.html', {'courses': courses, 'coaches': coaches})

def course_detail(request, slug):
    course = get_object_or_404(CourseType, slug=slug)
    return render(request, 'course_detail.html', {'course': course})

def coach_list(request):
    coaches = Coach.objects.all()  # 查询所有教练
    return render(request, 'coach_list.html', {'coaches': coaches})

def coach_detail(request, slug):
    coach = get_object_or_404(Coach, slug=slug)
    return render(request, 'coach_detail.html', {'coach': coach})

def beginner(request):
    return render(request, "beginner.html")


def competitive(request):
    return render(request, "competitive.html")


def onetoone(request):
    return render(request, "onetoone.html")


def zerodozen(request):
    return render(request, "zerodozen.html")


def summer(request):
    return render(request, "summer.html")


def winter(request):
    return render(request, "winter.html")


def elder(request):
    return render(request, "elder.html")


def ZZT(request):
    return render(request, "ZZT.html")


def HWH(request):
    return render(request, "HWH.html")


def CYZ(request):
    return render(request, "CYZ.html")


def ZBY(request):
    return render(request, "ZBY.html")


def power_ball(request):
    return render(request, "power_ball.html")


def left_right_ball(request):
    return render(request, "left_right_ball.html")


def small_ball(request):
    return render(request, "small_ball.html")


def community(request):
    return render(request, "community.html")


def mall(request):
    return render(request, "mall.html")


def shopingcar(request):
    return render(request, "shopingcar.html")

def course_Analysis_Registration(request):
    return render(request, "course_Analysis_Registration.html")


def course_Analysis(request):
    return render(request, "course_Analysis.html")


def member_center(request):
    return render(request, "member_center.html")


def payment(request):
    return render(request, "payment.html")

def list(request):
    return render(request, "list.html")


def reservation_list(request):
    return render(request, "reservation_list.html")



def registration_history(request):
    registrations = CourseRegistration.objects.filter(user=request.user)
    return render(request, "history.html")


def registration_history(request):
    registrations = CourseRegistration.objects.filter(user=request.user)
    return render(request, "history.html", {"registrations": registrations})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            verification_link = request.build_absolute_uri(
                f"/verify-email/{uid}/{token}/"
            )

            subject = "驗證您的電子信箱"
            message = render_to_string(
                "verify_email.html",
                {
                    "user": user,
                    "verification_link": verification_link,
                },
            )
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            return redirect("email_verification_sent")
        else:
            messages.error(request, "註冊失敗，請檢查您的輸入。")
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def email_verification_sent(request):
    return render(request, "email_verification_sent.html")


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "您的電子信箱已驗證，請登入。")
        return redirect("login")
    else:
        return HttpResponse("驗證連結無效或已過期。")


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            if not User.objects.filter(username=username).exists():
                messages.error(request, "此帳號尚未註冊，請先註冊。")
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "登入成功！")
                    return redirect("member_center")
                else:
                    messages.error(request, "帳號或密碼不正確，請再試一次。")
    else:
        form = UserLoginForm()

    return render(request, "login.html", {"form": form})


@login_required
def member_center(request):
    user = request.user
    form = MemberCenterForm(instance=user)
    return render(request, "member_center.html", {"form": form})


@login_required
def edit_member(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "編輯成功！")
            return redirect("member_center")
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, "edit_member.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


def member_redirect(request):
    if request.user.is_authenticated:
        return redirect("member_center")
    else:
        return redirect("login")


User = get_user_model()


def forgot_password(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            reset_link = request.build_absolute_uri(f"/reset-password/{uid}/{token}/")
            subject = "Reset your password"
            message = render_to_string(
                "reset_password_email.html",
                {
                    "reset_link": reset_link,
                    "user": user,
                },
            )
            send_mail(subject, message, "admin@example.com", [user.email])
            return render(request, "forgot_password_done.html")
        except User.DoesNotExist:
            return render(request, "forgot_password.html", {"error": "Email not found"})
    return render(request, "forgot_password.html")


def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "重設成功!!")
                return redirect("login")
            else:
                messages.error(request, "重設失敗!!")
        else:
            form = SetPasswordForm(user)
        return render(request, "reset_password.html", {"form": form})
    else:
        return render(request, "reset_password_invalid.html")


def community(request):
    posts = DiscussionPost.objects.all().order_by("-created_at")
    if request.method == "POST":
        if request.user.is_authenticated:
            form = DiscussionPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect("community")
        else:
            return redirect("login")
    else:
        form = DiscussionPostForm() if request.user.is_authenticated else None
    return render(request, "community.html", {"posts": posts, "form": form})


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(DiscussionPost, id=post_id)
    if request.method == "POST":
        form = DiscussionCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("community")
    return redirect("community")

# 編輯評論
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(DiscussionPost, id=post_id, author=request.user)

    if request.method == "POST":
        form = DiscussionPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("community")
    else:
        form = DiscussionPostForm(instance=post)

    return render(request, "edit_post.html", {"form": form, "post": post})


# 刪除評論
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(DiscussionPost, id=post_id, author=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("community")

    return render(request, "confirm_delete.html", {"post": post})


# 分析
teachers = [
    {
        "name": "蔡元振",
        "gender": "男生",
        "skills": ["單打四角拉吊"],
        "skills2": ["發球與接發球"],
        "incentives": ["運動健身"],
        "traits": ["有經驗", "理論基礎"],
    },
    {
        "name": "周仲庭",
        "gender": "女生",
        "skills": ["雙打輪轉"],
        "skills2": ["單打四角拉吊", "其他"],
        "incentives": ["運動健身"],
        "traits": ["有技術", "專業"],
    },
    {
        "name": "張秉洋",
        "gender": "男生",
        "skills": ["雙打後場組織進攻"],
        "skills2": ["發球與接發球", "其他"],
        "incentives": ["提升技巧"],
        "traits": ["有經驗", "專業", "嚴厲"],
    },
    {
        "name": "胡玟翰",
        "gender": "男生",
        "skills": ["發球與接發球"],
        "skills2": ["雙打後場組織進攻"],
        "incentives": ["參加比賽"],
        "traits": ["多元", "有技術"],
    },
]


def calculate_match(teacher, preferences):
    score = 0

    if preferences["gender"] != "不指定" and teacher["gender"] != preferences["gender"]:
        return 0

    for skill in preferences["skills"]:
        if skill in teacher["skills"]:
            score += 2

    for skill2 in preferences["skills2"]:
        if skill2 in teacher["skills2"]:
            score += 1

    for incentive in preferences["incentives"]:
        if incentive in teacher["incentives"]:
            score += 3

    for trait in preferences["traits"]:
        if trait in teacher["traits"]:
            score += 1

    return score


@csrf_protect
def recommend_teacher(request):
    if request.method == "POST":
        user_preferences = {
            "name": request.POST.get("name"),
            "birthday": request.POST.get("birthday"),
            "incentives": request.POST.getlist("motivation"),
            "gender": request.POST.get("coachGender", "不指定"),
            "skills": request.POST.getlist("techniques"),
            "traits": request.POST.getlist("coachTraits"),
        }

        teacher_scores = []
        for teacher in teachers:
            match_score = calculate_match(teacher, user_preferences)
            teacher_scores.append((teacher["name"], match_score))

        sorted_teachers = sorted(teacher_scores, key=lambda x: x[1], reverse=True)

        recommended_teachers = [
            (teacher, score) for teacher, score in sorted_teachers if score > 0
        ]
        for teacher, score in teacher_scores:
            print(f"{teacher}: {score}")

        return render(
            request,
            "recommend_result.html",
            {"recommended_teachers": recommended_teachers},
        )

    return redirect("course_Analysis_Registration")


def calculate_match(teacher, preferences):
    score = 0

    if preferences["gender"] != "不指定" and teacher["gender"] != preferences["gender"]:
        return 0

    for skill in preferences["skills"]:
        if skill in teacher["skills"]:
            score += 2

    for incentive in preferences["incentives"]:
        if incentive in teacher["incentives"]:
            score += 3

    for trait in preferences["traits"]:
        if trait in teacher["traits"]:
            score += 1

    return score


# 課程金額
COURSE_PRICES = {
    "兒童初階班(每週二14:00 - 15:30)": 4000,
    "兒童初階班(每週二15:30 - 17:00)": 4000,
    "成人初階班(每週一14:00 - 16:00)": 4000,
    "成人初階班(每週一16:00 - 18:00)": 4000,
    "一般競技班(每週二14:00 - 16:00)": 4000,
    "一般競技班(每週四16:00 - 18:00)": 4000,
    "進階競技班(每週四14:00 - 16:00)": 4000,
    "進階競技班(每週四16:00 - 18:00)": 4000,
    "基礎零打班(每週五19:00 - 22:00)": 350,
    "基礎零打班(每週六19:00 - 22:00)": 350,
    "進階零打班(每週五19:00 - 22:00)": 350,
    "進階零打班(每週六19:00 - 22:00)": 350,
    "個別班": 0,
}


@csrf_protect
def course_Registration(request):

    if not request.user.is_authenticated:
        messages.warning(request, "請先登入後再進行報名")
        return redirect("login")

    if request.method == "POST":
        selected_courses = request.POST.getlist("subCourseType")
        course_type = request.POST.getlist("courseType")
        total_cost = 0

        for course in selected_courses:
            total_cost += COURSE_PRICES.get(course, 0)

        if "個別班" in course_type:
            total_cost += 0

        return render(
            request,
            "course_result.html",
            {
                "total_cost": total_cost,
                "selected_courses": selected_courses,
                "course_type": course_type,
            },
        )

    return render(request, "course_Registration.html")



@csrf_protect
def course_result(request):
    if request.method == "POST":
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        birthday = request.POST.get("birthday")

        selected_courses = request.POST.getlist("subCourseType")
        course_type = request.POST.getlist("courseType")

        total_cost = calculate_total_cost(selected_courses)

        registration = CourseRegistration(
            user=request.user,
            course_type=", ".join(course_type),
            sub_course_type=", ".join(selected_courses),
            cost=total_cost,
        )
        registration.save()

        messages.success(request, "報名成功")

        context = {
            "name": name,
            "gender": gender,
            "phone": phone,
            "email": email,
            "birthday": birthday,
            "selected_courses": selected_courses,
            "total_cost": total_cost,
        }
        return render(request, "course_result.html", context)

    return render(request, "course_Registration.html")

def calculate_total_cost(sub_courses):
    prices = {
        "兒童初階班(每週二14:00 - 15:30)": 4000,
        "兒童初階班(每週二15:30 - 17:00)": 4000,
        "成人初階班(每週一14:00 - 16:00)": 4000,
        "成人初階班(每週一16:00 - 18:00)": 4000,
        "一般競技班(每週二14:00 - 16:00)": 4000,
        "一般競技班(每週四16:00 - 18:00)": 4000,
        "進階競技班(每週四14:00 - 16:00)": 4000,
        "進階競技班(每週四16:00 - 18:00)": 4000,
        "基礎零打班(每週五19:00 - 22:00)": 350,
        "基礎零打班(每週六19:00 - 22:00)": 350,
        "進階零打班(每週五19:00 - 22:00)": 350,
        "進階零打班(每週六19:00 - 22:00)": 350,
    }
    
    total = 0
    for course in sub_courses:
        total += prices.get(course, 0)
    
    return total

@csrf_exempt
@login_required
def create_order(request):
    if request.method == "POST":
        payer_name = request.POST.get("payer_name")
        payer_phone = request.POST.get("payer_phone")
        payer_email = request.POST.get("payer_email")
        payment_method = request.POST.get("payment_method")
        total_amount = request.POST.get("total_amount").replace(" 元", "")
        cart_data = request.POST.get("cart")  
        if cart_data is None:
            return HttpResponse("購物車資料未提供", status=400)

        try:
            cart = json.loads(cart_data)  
        except json.JSONDecodeError:
            return HttpResponse("無效的購物車資料", status=400)

        total_amount = Decimal(total_amount)

        order = Order.objects.create(
            user=request.user,
            payer_name=payer_name,
            payer_phone=payer_phone,
            payer_email=payer_email,
            payment_method=payment_method,
            total_amount=total_amount,
            paid=False,
        )

        order_items_with_totals = []  

        try:
            for item in cart:
                product_id = item['id']
                quantity = item.get('quantity', 1)  

                product = Product.objects.get(id=product_id)

                
                subtotal = product.price * quantity

                
                order_item = OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                )

                
                order_items_with_totals.append({
                    'product': product,
                    'quantity': quantity,
                    'price': product.price,
                    'subtotal': subtotal
                })

            order.save() 

            return render(request, "payment_success.html", {
                "order": order,
                "order_items_with_totals": order_items_with_totals  
            })

        except Product.DoesNotExist:
            return HttpResponse("商品未找到", status=404)
        except KeyError as e:
            return JsonResponse({'status': 'error', 'message': f'Missing key: {str(e)}'}, status=400)

    return render(request, "payment.html")



def payment_success(request, order_id):
    order = Order.objects.get(id=order_id)

    return render(request, "payment_success.html", {"order": order})


@login_required(login_url="/login/")
def course_result(request):
    if request.method == "POST":
        name = request.POST.get("name", "未提供")
        gender = request.POST.get("gender", "未提供")
        phone = request.POST.get("phone", "未提供")
        email = request.POST.get("email", "未提供")
        birthday = request.POST.get("birthday", "未提供")
        selected_courses = request.POST.getlist("subCourseType", [])
        total_cost = calculate_total_cost(selected_courses)

        if request.user.is_authenticated:
            registration = CourseRegistration(
                user=request.user,
                course_type=", ".join(request.POST.getlist("courseType")),
                sub_course_type=", ".join(selected_courses),
                cost=total_cost,
            )
            registration.save()

        context = {
            "name": name,
            "gender": gender,
            "phone": phone,
            "email": email,
            "birthday": birthday,
            "selected_courses": selected_courses,
            "total_cost": total_cost,
        }
        return render(request, "course_result.html", context)

def mall(request):
    products = Product.objects.all()  
    return render(request, 'mall.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def course_success_page(request):
    if request.method == "POST":
        name = request.POST.get('name', '未提供')
        gender = request.POST.get('gender', '未提供')
        phone = request.POST.get('phone', '未提供')
        email = request.POST.get('email', '未提供')
        birthday = request.POST.get('birthday', '未提供')
        selected_courses = request.POST.getlist('selected_courses', [])
        total_cost = request.POST.get('total_cost', 0)

        context = {
            'name': name,
            'gender': gender,
            'phone': phone,
            'email': email,
            'birthday': birthday,
            'selected_courses': selected_courses,
            'total_cost': total_cost
        }

        return render(request, 'course_success.html', context)

def reservation_list(request):
    coaches = Coach.objects.all()
    selected_coach_id = request.GET.get('coach_id')
    selected_date = request.GET.get('date')

    availabilities = CoachAvailability.objects.all()
    if selected_coach_id:
        availabilities = availabilities.filter(coach_id=selected_coach_id)
    if selected_date:
        availabilities = availabilities.filter(date=selected_date)

    return render(request, 'reservation_list.html', {
        'coaches': coaches,
        'availabilities': availabilities,
        'selected_coach_id': selected_coach_id,
        'selected_date': selected_date,
    })

def book_reservation(request):
    if request.method == 'POST':
        availability_id = request.POST.get('availability_id')
        student_name = request.POST.get('student_name')
        contact_info = request.POST.get('contact_info')

        availability = get_object_or_404(CoachAvailability, id=availability_id)
        if not availability.is_reserved:
            availability.is_reserved = True
            availability.reserved_by = student_name
            availability.contact_info = contact_info
            availability.save()
            messages.success(request, "預約成功！")
        else:
            messages.error(request, "該時段已被預約！")

    return redirect('reservation_list')


def book_time(request):
    coaches = Coach.objects.all()
    selected_coach_id = request.GET.get('coach_id')
    available_times = None

    # 設置過濾日期：今天之後
    filter_date = date.today() + timedelta(days=1)

    if selected_coach_id:
        available_times = CoachAvailability.objects.filter(
            coach_id=selected_coach_id,
            is_reserved=False,
            date__gte=filter_date  # 僅顯示明天及以後的時間
        )

    if request.method == 'POST':
        availability_id = request.POST.get('availability_id')
        student_name = request.POST.get('student_name')
        contact_info = request.POST.get('contact_info')

        availability = get_object_or_404(CoachAvailability, id=availability_id)
        if not availability.is_reserved:
            availability.is_reserved = True
            availability.reserved_by = student_name
            availability.contact_info = contact_info
            availability.save()
            messages.success(request, "預約成功！")
            return redirect('reservation_list')
        else:
            messages.error(request, "該時段已被預約！")

    return render(request, 'book_time.html', {
        'coaches': coaches,
        'available_times': available_times,
        'selected_coach_id': selected_coach_id,
    })
