# chat/urls.py
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # 例: /chat/room1/ にアクセスした時、views.room を呼び出す
    path('chat/<str:room_name>/', views.room, name='room'),
    path('', views.index, name="index")
]