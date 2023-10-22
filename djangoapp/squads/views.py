from rest_framework import viewsets
from .models import Squad
from .serializers import SquadSerializer, SquadListSerializer

class SquadViewSet(viewsets.ModelViewSet):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return SquadListSerializer
        return super().get_serializer_class()