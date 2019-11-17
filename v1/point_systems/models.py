from django.db import models


class PointSystem(models.Model):
    point_system_id = models.BigAutoField(primary_key=True, unique=True)
    is_enabled = models.BooleanField()
    points_per_cent = models.IntegerField()
    cents_per_points = models.IntegerField()