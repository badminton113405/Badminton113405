from rest_framework import generics, permissions
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CustomLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        print(f"Login attempt: username={username}, password={password}")  # 打印登录尝试信息

        # 确认用户存在
        user_exists = User.objects.filter(username=username).exists()
        if not user_exists:
            print(f"User {username} does not exist.")
            return Response({'error': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        # 认证用户
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UserSerializer(user).data})
        else:
            print(f"Authentication failed for username={username}")  # 打印失败原因
            print("User exists but password authentication failed.")
            return Response({'error': 'Unable to log in with provided credentials.'}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
