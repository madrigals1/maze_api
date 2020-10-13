from maze.models import Maze
from rest_framework import viewsets
from maze.serializers import MazeSerializer
from rest_framework.permissions import AllowAny


class MazeViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = MazeSerializer

    def get_queryset(self):
        return Maze.objects.all()
