import random
from copy import deepcopy

from src.constants import DO_NOT_INCLUDE, INCLUDE_SOLUTION_STEPS


class MazeGenerator:
    """ Class for generating Maze """

    def __init__(
        self, width, height, include_steps=False, solution_type=DO_NOT_INCLUDE
    ):

        # Array that will contain Maze
        self.maze = []

        # Actual size of the maze
        self.maze_width = width * 2 + 1
        self.maze_height = height * 2 + 1

        # Empty space (unvisited) count
        self.empty_space_count = width * height

        # Start position of X and Y
        self.cur_x = 1
        self.cur_y = 1

        # Hot directions, that will be used first when there will no directions to move
        self.other_directions = {}

        # Steps
        self.include_steps = include_steps
        self.steps = []

        # Solution
        self.solution_included = solution_type != DO_NOT_INCLUDE
        self.solution_steps_included = solution_type == INCLUDE_SOLUTION_STEPS

        # Run maze generation
        self.generate_maze()

    def generate_maze(
        self,
    ):
        """
        Code below will create walls 2D array like this

        1 1 1 1 1 1 1 1 1 1 1
        1 2 1 2 1 2 1 2 1 2 1
        1 1 1 1 1 1 1 1 1 1 1
        1 2 1 2 1 2 1 2 1 2 1
        1 1 1 1 1 1 1 1 1 1 1
        1 2 1 2 1 2 1 2 1 2 1
        1 1 1 1 1 1 1 1 1 1 1
        1 2 1 2 1 2 1 2 1 2 1
        1 1 1 1 1 1 1 1 1 1 1

        Here, 1 represent wall and 2 represent empty space to be visited
        """
        for i in range(self.maze_width):
            self.maze.append([])
            for j in range(self.maze_height):
                # If i or j are borders, create wall
                if i in (0, self.maze_width - 1) or j in (0, self.maze_height - 1):
                    self.maze[i].append(1)
                # If index of i or j are even, create wall
                elif not i % 2 or not j % 2:
                    self.maze[i].append(1)
                # If index of i and j are both odd, create empty space
                else:
                    self.maze[i].append(2)

        # Add step before creation of the maze
        self.add_step()

        # Visit initial position
        self.maze[self.cur_x][self.cur_y] = 0
        self.empty_space_count -= 1

        # Add step after first position visit
        self.add_step()

        # While there are points, that we haven't visited, keep walking
        while self.empty_space_count:
            directions = self.find_directions()

            if directions:
                direction_key = random.choice(list(directions.keys()))
                # Pick random directions from provided
                direction = directions.pop(direction_key)

                # Add directions, that are left to hot directions
                self.other_directions.update(directions)
            else:
                # Pick first of hot directions
                direction_key = random.choice(list(self.other_directions.keys()))

                direction = self.other_directions.pop(direction_key)

            self.move(position=direction_key, wall=direction)

            # Add step after each move
            self.add_step()

        return {"maze": self.maze, "solution": self.maze, "steps": self.steps}

    def find_directions(self):
        """ Find all directions that walker can move """

        # Directions that walker can move
        directions = {}

        # Right
        if (
            self.cur_x + 1 != self.maze_width - 1
            and self.maze[self.cur_x + 2][self.cur_y] != 0
        ):
            directions[(self.cur_x + 2, self.cur_y)] = self.cur_x + 1, self.cur_y

        # Left
        if self.cur_x - 1 != 0 and self.maze[self.cur_x - 2][self.cur_y] != 0:
            directions[(self.cur_x - 2, self.cur_y)] = self.cur_x - 1, self.cur_y

        # Down
        if (
            self.cur_y + 1 != self.maze_height - 1
            and self.maze[self.cur_x][self.cur_y + 2] != 0
        ):
            directions[(self.cur_x, self.cur_y + 2)] = self.cur_x, self.cur_y + 1

        # Up
        if self.cur_y - 1 != 0 and self.maze[self.cur_x][self.cur_y - 2] != 0:
            directions[(self.cur_x, self.cur_y - 2)] = self.cur_x, self.cur_y - 1

        return directions

    def move(self, position, wall):
        """ Walker move in specific direction """

        # Get X and Y
        self.cur_x, self.cur_y = position
        wall_x, wall_y = wall

        # Break the wall of this direction
        self.maze[wall_x][wall_y] = 0

        # Set the current X and Y and visit them
        self.maze[self.cur_x][self.cur_y] = 0

        # Remove just visited positions from Hot visit positions
        self.other_directions.pop((self.cur_x, self.cur_y), None)

        # Decrease amount of empty spaces to be visited
        self.empty_space_count -= 1

    def print_maze(self):
        """ Method for printing Maze """

        maze_str = ""

        for i in range(self.maze_width):
            for j in range(self.maze_height):
                maze_str += str(self.maze[i][j]) + " "
            maze_str += "\n"

        print(maze_str)

    def add_step(self):
        """ Add each step of maze creation """

        if self.include_steps:
            self.steps.append(deepcopy(self.maze))
