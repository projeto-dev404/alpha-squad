from django.contrib import admin

from .models import Stack


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    pass
