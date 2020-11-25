from flask import Flask, jsonify, request

from src.constants import DO_NOT_INCLUDE
from src.services import MazeGenerator

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(detail="Maze API is working. Use /create to create maze")


@app.route("/maze", methods=["POST", "GET"])
def convert():
    if request.method == "GET":
        return jsonify(
            detail="Please, make POST request and provide 'width' and 'height' in request body"
        )

    data = request.json
    width = data.get("width")
    height = data.get("height")
    include_steps = data.get("include_steps", False)
    solution_type = data.get("solution_type", DO_NOT_INCLUDE)

    if not width or not height:
        return jsonify(detail="Please, provide 'width' and 'height' in request body")

    maze_object = MazeGenerator(
        width=width,
        height=height,
        include_steps=include_steps,
        solution_type=solution_type,
    )

    return {"maze": maze_object.maze}
