# views.py
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404
from rest_framework import status


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

def login(request):
    return HttpResponse("Login view")

@csrf_exempt
def register(request):
    print("test")
    return HttpResponse("Register view")

def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    user = get_object_or_404(User, email=email)
    
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_link = request.build_absolute_uri(
        reverse('reset-password-confirm', kwargs={'uidb64': uid, 'token': token})
    )

    send_mail(
        'Password Reset Request',
        f'Use the link below to reset your password: {reset_link}',
        'noreply@example.com',
        [user.email],
        fail_silently=False,
    )

    return Response({'message': 'Password reset link has been sent to your email.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        password = request.data.get('password')
        user.set_password(password)
        user.save()
        return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid link or token'}, status=status.HTTP_400_BAD_REQUEST)
