from django.db import models


class PointSystemManager(models.Manager):
    def create_point_system(self, points_per_cent, cents_per_point, is_enabled=True):
        point_system = self.model(is_enabled=is_enabled, points_per_cent=points_per_cent,
                                  cents_per_point=cents_per_point)
        point_system.save(using=self._db)

        return point_system


class PointSystem(models.Model):
    objects = PointSystemManager()

    point_system_id = models.BigAutoField(primary_key=True, unique=True)
    is_enabled = models.BooleanField()
    points_per_cent = models.IntegerField()
    cents_per_point = models.IntegerField()