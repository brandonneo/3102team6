from flask import Blueprint, jsonify, request
from domain.BeaconControl import BeaconControl
import random

# Initialization
router = Blueprint("BeaconRoutes", __name__)

BeaconControl = BeaconControl()


@router.route("/extractbeacon", methods=['GET', 'POST'])
def extractBeacon():
    try:
        staff_id = int(request.args.get('staff_id'))
        start_time = int(request.args.get('start_time'))
        end_time = int(request.args.get('end_time'))

        locations = BeaconControl.retrieve_staff_location(
            staff_id, start_time, end_time)
        return jsonify({
            "location": locations
        })
    except:
        return jsonify({"location": "Invalid get params"})

@router.route("/newbeacondetect", methods=['GET', 'POST'])
def newBeaconDetect():
    try:
        staff_id = int(request.args.get('staff_id'))
        beacon_address = request.args.get('beacon_address')
        rssi = int(request.args.get('rssi'))
        BeaconControl.new_beacon_detect(staff_id, beacon_address, rssi)
        return f"New Beacon Detection Added"
    except:
        return jsonify({"location": "Invalid get params"})