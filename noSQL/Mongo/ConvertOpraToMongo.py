#!/usr/bin/env python

import re, json
from pymongo import MongoClient

# This script converts Opra file into Dictionary then to JSON for loading into Mongo

opra=open("opra_example_regression.log","r")

coreData=[]
for line in opra.readlines():
    print(".",end="")
    line=line.strip()
    if re.search(r"^Info:", line):
        # Split into Mongo read data
        info=line.split(": ")
        if len(info) < 3:
            continue
        coreData.append({"MessageType": info[0], "action": info[1].lstrip(), "message": info[2].lstrip()})
    if re.search(r"^Error:", line):
        error=line.split(": ")
        if len(error) < 3:
            continue
        coreData.append({"MessageType": error[0], "action": error[1].lstrip(), "message": error[2].lstrip()})
    if re.search(r"^Regression:", line):
        if "Record Publish" in line:
            try:
                if len(list(tmpData.keys())) > 1:
                    tmpData.update({"MessageType": "Record Publish", "Ticker": oldTicker})
                    coreData.append(tmpData)
                    coreData["Regression"].append(tmpData)
                    tmpData={}
            except:
                tmpData={}
            data=line.split(": ")
            tmpData["Ticker"]=data[2]
            oldTicker=data[2]
        if "Type:" in line:
            data=re.split(r": +", line)
            tmpData[data[1]]=data[2]
        if re.search(r"^Regression: +w[A-Z]", line):
            data=re.split(r": +", line)
            data=data[1].split(" | ")
            if len(data) < 4:
                data.append("null")
            tmpData[data[0]] = [ data[1], data[2], data[3]]

print()
opra.close()

# jsonData=json.dumps(coreData)
# print(jsonData)
# jOut=open("mongo-opra.json","w")
# jOut.write(jsonData)
# jOut.close()

myclient = MongoClient("mongodb://localhost:32768/")
db = myclient["opra"]
Collection=db["regression"]
Collection.insert_many(coreData)
