from django.shortcuts import render
from rest_framework import viewsets
from djoser.serializers import UserSerializer
from .models import Stack


class StackViewSet(viewsets.ModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = UserSerializer