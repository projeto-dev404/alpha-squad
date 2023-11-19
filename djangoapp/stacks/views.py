from rest_framework import viewsets
from stacks.models import Stack
from stacks.serializers import StackListSerializer, StackSerializer


class StackViewSet(viewsets.ModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return StackListSerializer
        return super().get_serializer_class()
