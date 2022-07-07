import logging

from flask import Flask, request, render_template, send_from_directory
from main_bp.views import main_bp_blueprint
from loader_bp.views import loader_bp_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(loader_bp_blueprint)
app.register_blueprint(main_bp_blueprint)

logging.basicConfig(filename='basic.log', level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()

