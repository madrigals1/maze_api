from django.db import models
from maze.services import MazeGenerator
from maze.constants import SOLUTION_TYPES, DO_NOT_INCLUDE


class Maze(models.Model):
    """ Model for Maze """

    width = models.IntegerField(default=20)
    height = models.IntegerField(default=20)
    maze_json = models.JSONField(default=dict)

    # Do we include creation steps into Maze JSON
    include_steps = models.BooleanField(default=False)

    # Normal, Include Solution of Include Solution + Solution Steps
    solution_type = models.CharField(
        default=DO_NOT_INCLUDE, choices=SOLUTION_TYPES, max_length=255
    )

    def save(self, *args, **kwargs):
        maze_generator = MazeGenerator(
            width=self.width,
            height=self.height,
            include_steps=self.include_steps,
            solution_type=self.solution_type,
        )
        self.maze_json = maze_generator.generate_maze()
        super().save(*args, **kwargs)

    class Meta:
        app_label = "maze"
