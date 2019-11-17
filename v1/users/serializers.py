from rest_framework import serializers
from DigiWallet.settings import AUTH_USER_MODEL


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AUTH_USER_MODEL
        fields = ['user_id', 'email', 'first_name', 'last_name', 'user_type', 'date_created', 'last_login', 'is_active']
