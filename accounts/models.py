from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # AbstractUserを継承してそのまま使用
    # ＊本来ならユーザー名やパスワードを指定
    pass