import pymongo
from datasource.Database import Database
import time
class StaffGateway:
    # Static
    __StaffCollection = Database.db["staff"]

    # Get all staff locations withint the 24 hour period
    def retrieve_all_staff(self):
        collection = StaffGateway.__StaffCollection
        end_timestamp = int(time.time())
        start_timestamp = end_timestamp - 86400 #24 hour record
        return list(collection.find({"timestamp": {"$gte": start_timestamp, "$lte": end_timestamp }}).sort("timestamp", -1))

    # retrieve all locations detected within the timestamp for one user
    def retrieve_staff_location(self, id, start_time, end_time):
        collection = StaffGateway.__StaffCollection
        allStaffVisitedLocations = collection.find({"staff_id": id})
        temp = []
        for item in allStaffVisitedLocations:
            # if timestamp is greater then the endtime, break out of the loop. Dont need to check the rest
            if int(item["timestamp"]) > end_time:
                break
            if start_time <= int(item["timestamp"]) <= end_time:
                item.pop('_id', None)
                item.pop('rssi', None)
                item.pop('mac', None)
                item.pop('staff_id', None)
                temp.append(item)
        return temp

    # add new location based on user and detected beacon to the db
    def add_new_staff_location(self, staff_id, level, location, rssi, beacon_address):
        new_location = {
            "level": level,
            "location": location,
            "timestamp": int(time.time()),
            "rssi": rssi,
            "mac": beacon_address,
            "staff_id": staff_id
        }
        collection = StaffGateway.__StaffCollection
        try:
            collection.insert_one(
                new_location
            )
            return True
        except Exception as e:
            print(e)
