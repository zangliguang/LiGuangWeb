# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from ecommerce.models import user


class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'birthday', 'email', 'image')
    list_filter = ('birthday',)  # 页面右边会出现相应的过滤器选项
    ordering = ('birthday',)  # 排序


admin.site.register(user, UserAdmin)
