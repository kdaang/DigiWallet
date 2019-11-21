from rest_framework import serializers
from v1.cards.serializers import CardSerializer
from v1.customers.models import Customer
from v1.users.serializers import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    card = CardSerializer(required=False)

    class Meta:
        model = Customer
        fields = ['user', 'customer_id', 'card']

    def create(self, validated_data):
        return Customer.objects.signup(**validated_data)