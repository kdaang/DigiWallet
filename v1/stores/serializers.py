from rest_framework import serializers
from v1.stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'company']

    def create(self, validated_data):
        return Store.objects.register(**validated_data)

    # TODO: DEF UPDATE
