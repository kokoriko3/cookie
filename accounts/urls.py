# accounts/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    # サインアップ画面
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # ログイン画面（Djangoの標準機能を使用）
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # ログアウト機能（画面は持たず、処理だけ行います）
    path('logout/', LogoutView.as_view(), name='logout'),
]