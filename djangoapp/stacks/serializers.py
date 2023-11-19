from rest_framework import serializers

from .models import Stack


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ['id', 'name', 'squads']


class StackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ['id', 'name']
