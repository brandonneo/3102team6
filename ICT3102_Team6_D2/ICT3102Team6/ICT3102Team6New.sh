#!/bin/bash
DIR="ICT3102_Team6/"
if [ -d "$DIR" ]; then rm -rf $DIR; fi
git clone https://github.com/raypal4/ICT3102_Team6.git
cd ICT3102_Team6
docker-compose -f docker-compose1.yaml up --build -d
cd ..
#docker run --rm --volumes-from mongodb -v $(pwd):/backup busybox tar xvf /backup/backup.tar data/
sleep 10
docker exec -it cfgsvr1 mongo --eval 'rs.initiate({_id: "cfgrs", configsvr: true, members: [{_id: 0, host: "172.17.0.1:40001", priority: 2}]})'
sleep 5
docker exec -it s1 mongo --eval 'rs.initiate({_id: "shards1", members: [{_id: 0, host: "172.17.0.1:50001", priority: 2}]})'
sleep 5
docker exec -it s3 mongo --eval 'rs.initiate({_id: "shards2", members: [{_id: 0, host: "172.17.0.1:50003", priority: 2}]})'
sleep 5
docker exec -it mongos1 mongo --host 172.17.0.1 --port 27018 --eval 'sh.addShard("shards1/172.17.0.1:50001")'
sleep 5
docker exec -it mongos1 mongo --host 172.17.0.1 --port 27018 --eval 'sh.addShard("shards2/172.17.0.1:50003")'
sleep 5
docker exec -it mongos1 mongo --host 172.17.0.1 --port 27018 --eval 'db.createCollection("staff")'
sleep 5
docker exec -it mongos1 mongo --host 172.17.0.1 --port 27018 --eval 'db.createCollection("beacons")'
sleep 5
docker exec -it mongos1 mongo --host 172.17.0.1 --port 27018 --eval 'sh.enableSharding("ICT3102")'
sleep 5
docker exec -it mongos1 mongo --host 172.17.0.1 --port 27018 --eval 'sh.shardCollection("ICT3102.staff", {"staff_id":"hashed"})'
sleep 5
docker exec -it mongos1 mongo --host 172.17.0.1 --port 27018 --eval 'sh.shardCollection("ICT3102.beacons", {"level":"hashed"})'
sleep 5
docker cp beacons.json mongos1:/beacons.json
sleep 5
docker exec -it mongos1 mongoimport --db ICT3102 --collection beacons --file beacons.json --jsonArray