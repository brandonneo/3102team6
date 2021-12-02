from flask import Flask, render_template
from routes import (
    BeaconRoutes,
)
from domain.BeaconControl import BeaconControl
from waitress import serve

app = Flask(__name__)
# Configuration
app = Flask(
    __name__,
    static_url_path="/",
    static_folder="static",
    template_folder="templates",
)


@app.route("/")
def index():
    data = BeaconControl().retrieve_all_staff()
    return render_template("index.html", data=data)


app.register_blueprint(BeaconRoutes.router)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
