from django.contrib import admin
from stacks.models import StackOnSquad

from .models import Squad, UsersOnSquads


class UsersOnSquadsInline(admin.TabularInline):
    model = UsersOnSquads


class StackOnSquadInline(admin.TabularInline):
    model = StackOnSquad


@admin.register(Squad)
class SquadAdmin(admin.ModelAdmin):
    inlines = [UsersOnSquadsInline, StackOnSquadInline]
