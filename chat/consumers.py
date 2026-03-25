# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room, Message

class ChatConsumer(WebsocketConsumer):
    # WebSocketに接続された時の処理
    def connect(self):
        # URLからルーム名を取得
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # グループ（チャットルーム）に参加
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    # WebSocketから切断された時の処理
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # ブラウザからメッセージを受け取った時の処理
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope['user']

        # ログインしている場合のみデータベースに保存
        if user.is_authenticated:
            room = Room.objects.get(name=self.room_name)
            Message.objects.create(user=user, room=room, content=message)
            username = user.username
        else:
            username = "名無し"

        # グループ内の全員にメッセージを送信
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # グループからメッセージを受け取ってブラウザに送る処理
    def chat_message(self, event):
        self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username']
        }))