from django.db import models


class Maze(models.Model):

    width = models.IntegerField(default=20)
    height = models.IntegerField(default=20)
    matrix = models.JSONField(default=dict)

    class Meta:
        app_label = "maze"
