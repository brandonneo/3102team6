from flask import Flask, render_template
from routes import (
    BeaconRoutes,
)
from waitress import serve
from flask_cors import CORS

app = Flask(__name__)
# Configuration
app = Flask(
    __name__,
    static_url_path="/",
    static_folder="static",
    template_folder="templates",
)
CORS(app)

@app.route("/")
def index():
    return "API Server Started"

app.register_blueprint(BeaconRoutes.router)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
