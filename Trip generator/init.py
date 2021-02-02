# coding=utf-8
from datetime import datetime, timedelta
import random
import requests
import string

url = "http://localhost:9234/records"

locationsRijeka = [
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
    "Rijeka"]

locationsSplit = [
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

def createTrip(numOfSections=2, locationIndex=0, locations=locationsSplit, plate='ZG123NN', startTime=datetime.now() ,direction='A'):
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

def createPlateMark(registerUser=False):
    if(registerUser):
        return 'ZG2222LL'
    towns= ['ZG', 'BJ', 'BM', 'ČK', 'DA', 'DE', 'DJ', 'DU', 'GS', 'IM', 'KA', 'KC', 'KR', 'KT', 'KŽ', 'MA', 'NA', 'NG', 'OG', 'OS', 'PU', 'PŽ', 'RI', 'SB', 'SK', 'SL', 'ST', 'ŠI', 'VK', 'VT', 'VU', 'VŽ', 'ZD', 'ŽU']
    num = random.randint(100,9999)
    lett = random.choice(string.ascii_letters).upper()
    lett += random.choice(string.ascii_letters).upper()
    return towns[random.randint(0,len(towns) -1)] + str(num) +lett

def rndTime():
    return datetime.now() - timedelta(days=random.randint(0,150),hours=random.randint(0,20))

def rndSects():
    return random.randint(2,28)

def rndLct():
    return random.randint(0,30)



trips = []

for i in range(0,100):
    trips.extend(createTrip(plate=createPlateMark(),numOfSections=rndSects(), locationIndex=rndLct(),startTime=rndTime()))

trips.extend(createTrip(plate=createPlateMark(True),numOfSections=rndSects(), locationIndex=rndLct(),startTime=rndTime()))

headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
response = requests.post(url = url, headers=headers, json=trips,  verify=False)

print response
