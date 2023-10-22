from rest_framework import serializers
from .models import Squad, UsersOnSquads
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')
        ref_name = 'UserSerializer'

class UsersOnSquadsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    role = serializers.CharField(source='userRoleOnSquad')
    squad = serializers.SerializerMethodField()
    ref_name = 'UsersOnSquadsSerializer'

    class Meta:
        model = UsersOnSquads
        fields = ('user', 'role', 'squad')

    def get_squad(self, obj):
        return obj.squad.name

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_representation = representation.pop('user')
        return {
            'id': user_representation['id'],
            'name': user_representation['name'],
            'email': user_representation['email'],
            'squad': representation['squad'],
            'role': representation['role']
        }

class SquadSerializer(serializers.ModelSerializer):
    users_on_squad = UsersOnSquadsSerializer(many=True, read_only=True)

    class Meta:
        model = Squad
        fields = ('id', 'name', 'description', 'users_on_squad')
        lookup_field = 'id'

class SquadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squad
        fields = ('id', 'name', 'description')
        lookup_field = 'id'