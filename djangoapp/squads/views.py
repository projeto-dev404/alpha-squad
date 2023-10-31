from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Squad, UsersOnSquads
from .serializers import SquadSerializer, SquadListSerializer, UsersOnSquadsSerializer

class SquadViewSet(viewsets.ModelViewSet):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return SquadListSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied('Você não tem permissão para criar squads.')
        serializer.save()