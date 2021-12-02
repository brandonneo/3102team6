from flask import Flask, render_template, jsonify
from waitress import serve
from flask_cors import CORS, cross_origin

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
    return "Reached Monitoring Server"

@app.route("/monitoring")
def monitoring():
    return render_template("index.html")

@app.route("/extractbeacon", methods=['GET', 'POST'])
@cross_origin(origin='*')
def error_extract():
    return jsonify({
        "data": "Flask servers circuit breaker open."
    })

@app.route("/retrieveformonitoring", methods=['GET', 'POST'])
@cross_origin(origin='*')
def error_retrieve():
    return jsonify({
        "data": "Flask servers circuit breaker open."
    })

@app.route("/newbeacondetect", methods=['GET', 'POST'])
@cross_origin(origin='*')
def error_newBeaconDetect():
    return jsonify({
        "data": "Flask servers circuit breaker open."
    })
    
if __name__ == "__main__":
    # NGINX ver TODO remove port 80
    serve(app, host='0.0.0.0', port=4000)
