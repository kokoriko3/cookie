# chat/models.py
from django.db import models
from django.conf import settings

# チャットルームのモデル
class Room(models.Model):
    name = models.CharField(verbose_name='ルーム名', max_length=255, unique=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        return self.name

# メッセージのモデル
class Message(models.Model):
    # どのルームでの発言か
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    # 誰の発言か（settings.AUTH_USER_MODELで現在のユーザーモデルと紐付けます）
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 発言内容
    content = models.TextField(verbose_name='メッセージ内容')
    # 発言日時
    created_at = models.DateTimeField(verbose_name='送信日時', auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.content[:20]}'