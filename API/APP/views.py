from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Member, Message, Coach, Course, Reservation
import json

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer


@csrf_exempt
def register_member(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        
        if not username or not password or not email:
            return JsonResponse({'error': 'Missing fields'}, status=400)

        if Member.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        
        member = Member(username=username, password=make_password(password), email=email)
        member.save()
        
        return JsonResponse({'message': 'Member registered successfully'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def create_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        member_id = data.get('member_id')
        content = data.get('content')

        if not member_id or not content:
            return JsonResponse({'error': 'Missing fields'}, status=400)
        
        try:
            member = Member.objects.get(id=member_id)
        except Member.DoesNotExist:
            return JsonResponse({'error': 'Member not found'}, status=404)
        
        message = Message(member=member, content=content)
        message.save()
        
        return JsonResponse({'message': 'Message created successfully'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def test(request):
    print("test")
    try:
        data = json.loads(request.body)
        member_id = data.get('memberId')
        course_id = data.get('courseId')
        reservation_date = data.get('reservationDate')

        member = Member.objects.get(id=member_id)
        course = Course.objects.get(id=course_id)

        Reservation.objects.create(
            member=member,
            course=course,
            reservation_date=reservation_date
        )

        return JsonResponse({'message': 'Reservation created successfully'}, status=201)
    except Member.DoesNotExist:
        return JsonResponse({'error': 'Member not found'}, status=404)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
