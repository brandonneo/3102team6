#!/bin/bash
DIR="ICT3102_Team6/"
if [ -d "$DIR" ]; then rm -rf $DIR; fi
git clone https://github.com/raypal4/ICT3102_Team6.git
cd ICT3102_Team6
docker-compose -f docker-compose2.yaml up --build -d
cd ..
sleep 10
docker exec -it mongo mongo --host 172.17.0.1 --port 27017 --eval 'db.createCollection("staff")'
sleep 5
docker exec -it mongo mongo --host 172.17.0.1 --port 27017 --eval 'db.createCollection("beacons")'
sleep 5
docker cp beacons.json mongo:/beacons.json
sleep 5
docker exec -it mongo mongoimport --db ICT3102 --collection beacons --file beacons.json --jsonArray