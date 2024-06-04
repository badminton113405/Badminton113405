from django.core.management.base import BaseCommand
from APP.models import User  # 导入你的自定义用户模型
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create a User superuser'

    def handle(self, *args, **options):
        name = input("Enter id(phonenumber): ")
        nickname = input("Enter nickname: ")
        gender = input("Enter gender: ")
        email = input("Enter email: ")
        birth_date = input("Enter email: ")
        phone = input("Enter phone: ")
        username = input("Enter username")
        password = input("Enter password: ")



        User.objects.create_superuser(
            full_name = name,
            username =username,
            password=password,
            nickname = nickname,
            gender = gender,
            email = email,
            birth_date =birth_date,
            phone =phone,
            is_staff=True,
            is_superuser=True,
            date_joined=timezone.now()
        )

        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
