from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id']
        read_only_fields = ['score']

class UserWithTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'token']
