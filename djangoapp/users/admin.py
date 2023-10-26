from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from squads.models import UsersOnSquads

from .models import User


class UsersOnSquadsInline(admin.TabularInline):
    model = UsersOnSquads


class CustomUserAdmin(UserAdmin):
    inlines = (UsersOnSquadsInline,)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )
    list_display = ('email', 'name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'name', 'email')
    ordering = ()
    filter_horizontal = (
        'groups',
        'user_permissions',
    )


admin.site.register(User, CustomUserAdmin)