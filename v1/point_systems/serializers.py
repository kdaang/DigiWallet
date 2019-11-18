from rest_framework import serializers
from v1.point_systems.models import PointSystem


class PointSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointSystem
        fields = ['point_system_id', 'is_enabled', 'points_per_cent', 'cents_per_point']