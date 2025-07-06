from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser
    list_display = ('username', 'last_login', 'date_joined', 'first_name', 'last_name')
    list_filter = ('username',)
    ordering = ('username', 'date_joined')

    fieldsets = (
        (None, {'fields': ('username',)}),
        (('perfil'), {'fields': ('image', 'first_name', 'last_name')}),
        (('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
