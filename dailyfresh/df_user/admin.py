from django.contrib import admin
from .models import *
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uname','upwd','uemail']#出现列表中显示的字段

admin.site.register(UserInfo,UserInfoAdmin)
