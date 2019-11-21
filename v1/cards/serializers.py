from rest_framework import serializers
from v1.cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = 'card_id, is_enabled'

