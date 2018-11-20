from rest_framework import serializers

from .models import ServerInfo, UserInfo


class ServerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInfo
        fields = ("id", "name", "host", "port", "server_type")


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("server", "name", "password")
