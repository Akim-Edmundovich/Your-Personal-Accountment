from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Поля для отображения в списке пользователей в админке
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    # Поля, по которым можно искать в админке
    search_fields = ('email', 'first_name', 'last_name')

    # Фильтры по этим полям
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Стандартные поля для редактирования
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups',
            'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Поля, которые запрашиваются при создании пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    # Поле, которое будет использоваться для логина
    ordering = ('email',)
