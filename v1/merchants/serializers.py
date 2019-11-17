from rest_framework import serializers
from v1.merchants.models import Merchant
from v1.users.serializers import UserSerializer


class MerchantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Merchant
        fields = ['user', 'company_id', 'company_name', 'point_system']

    # def create(self, validated_data):
