from flask import jsonify
from datasource.Database import Database


class BeaconGateway:
    # Static
    __BeaconCollection = Database.db["beacons"]

    # retrieve beacon location based on mac address
    def get_location_details(self, beacon_address):
        collection = BeaconGateway.__BeaconCollection
        beacon = collection.find_one({"mac_address": beacon_address})
        beaconLocation = beacon["location"]
        beaconLevel = beacon["level"]
        return {
            "beaconLocation": str(beaconLocation),
            "beaconLevel": str(beaconLevel)
        }
