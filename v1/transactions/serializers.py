from rest_framework import serializers
from v1.transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'date_created', 'from_user', 'to_user', 'total']

    def create(self, validated_data):
        return Transaction.objects.create_transaction(**validated_data)

