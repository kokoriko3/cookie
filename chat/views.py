# chat/views.py
from django.shortcuts import render
from .models import Room

def room(request, room_name):
    # ルームが存在しなければ新規作成し、存在すれば取得する
    chat_room, created = Room.objects.get_or_create(name=room_name)
    
    # このルームの過去のメッセージを古い順に取得
    messages = chat_room.messages.order_by('created_at')

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages,
    })

def index(request):
    return render(request, 'chat/index.html')