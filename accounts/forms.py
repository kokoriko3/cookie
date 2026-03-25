from django.contrib.auth.forms import UserCreationForm
# models.pyのカスタムUserをインポート
from .models import CustomUser

# カスタムUserモデルとの連携、４つのフィールドの指定を行う
class CustomUserCreationForm(UserCreationForm):
    class Meta:

        model = CustomUser
        # フォームで使用するフィールドを指定
        fields = ('username', 'email')