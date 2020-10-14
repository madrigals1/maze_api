from maze.models import Maze
from rest_framework import serializers


class MazeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maze
        fields = [
            "id",
            "width",
            "height",
            "maze_json",
            "include_steps",
            "solution_type",
        ]
        read_only_fields = ["maze_json"]
