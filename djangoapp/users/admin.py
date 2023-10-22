from django.contrib import admin
from .models import User
from squads.models import UsersOnSquads

class UsersOnSquadsInline(admin.TabularInline):
    model = UsersOnSquads

class CustomUserAdmin(admin.ModelAdmin):
    inlines = (UsersOnSquadsInline,)

# Register your models here.

admin.site.register(User, CustomUserAdmin)