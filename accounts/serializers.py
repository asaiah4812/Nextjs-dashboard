from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']

class ProfileSerializer(serializers.Serializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user', 'email', 'image', 'realname', 'location', 'bio']