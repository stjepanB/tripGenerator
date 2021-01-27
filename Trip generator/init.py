# coding=utf-8
from datetime import datetime, timedelta
import random
import requests

url = "http://localhost:9234/records"

locations = [
    "Lučko",
    "Zdenčina",
    "Jastrebarsko",
    "Karlovac",
    "Novigrad",
    "Bosiljevo",
    "Vrbovsko",
    "Ravna",
    "Delnice",
    "Vrata",
    "Oštrovica",
    "Rijeka",
    "Lučko",
    "Zdenčina",
    "Jastrebarsko",
    "Karlovac",
    "Novigrad",
    "Bosiljevo",
    "Ogulin",
    "Brinje",
    "Žuta",
    "Otočac",
    "Perušić",
    "Gospić",
    "Gornja",
    "Sveti",
    "Maslenica",
    "Posedarje",
    "Zadar Zapad",
    "Zadar Istok",
    "Benkovac",
    "Pirovac",
    "Skradin",
    "Šibenik",
    "Vrpolje",
    "Prgomet",
    "Vučevica",
    "Dugopolje",
    "Bisko",
    "Blato",
    "Šestanovac",
    "Zagvozd",
    "Ravča",
    "Vrgorac",
    "Karamatići",
]

def createDateTime(startTime, numOfSectionsPassed=0):
    if(numOfSectionsPassed == 0):
        min = random.randint(11, 25)
        new_time = startTime + timedelta(minutes=min)
        return new_time
    arr = []
    for i in range(numOfSectionsPassed):
        min = random.randint(11,25)
        new_time = startTime + timedelta(minutes=min)
        arr.append(new_time)
        startTime = new_time
    return arr

def timeToString(time):
    #2021-01-26T13:09:59.268Z
    #2021-01-26T14:50:39.522000
    #2021-01-26T14:32:05Z
    #2021-01-26T14:30:28.000Z
    dt_string = time.strftime("%Y-%m-%d %H:%M")
    return time.isoformat()

def createRecord(plate, time, location):
    record = {
        "id": "",
        "recordedTime": time,
        "plateMark": plate,
        "location": location,
    }
    return record


def createTrip(numOfSections=2, locationIndex=0, plate='ZG123NN', startTime=datetime.now() ,direction='A'):
    arr=[]
    if(direction == 'A'):
        for time in createDateTime(startTime,numOfSections):
            arr.append(createRecord(plate,timeToString(time),locations[locationIndex]))
            locationIndex+= 1
            if(locationIndex >= len(locations)):
                break
        return arr
    else:
        for time in createDateTime(startTime, numOfSections):
            arr.append(createRecord(plate,timeToString(time),locations[locationIndex]))
            locationIndex-= 1
            if(locationIndex < 0):
                break
        return arr


d = createTrip(plate='ST2212LP',numOfSections=10)
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
requests.post(url = url, headers=headers, json=d,  verify=False)


