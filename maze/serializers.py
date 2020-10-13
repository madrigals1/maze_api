from maze.models import Maze
from rest_framework import serializers


class MazeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maze
        fields = ["id", "width", "height", "matrix"]
        read_only_fields = ["matrix"]
