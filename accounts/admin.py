from django.contrib import admin
from .models import CustomUser
"""管理ページのレコード一覧に表示するカラムを管理"""""
class CustomUserAdmin(admin.ModelAdmin):
    # レコード一覧にusernameを表示
    list_display = ('id','username')
    # 表示するカラムにリンクを設定
    list_display_links=('id','username')

admin.site.register(CustomUser, CustomUserAdmin)