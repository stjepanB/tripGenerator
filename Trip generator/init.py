#import requests
from datetime import datetime
url = "http://localhost:9234/record"

 #datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d-%m-%YT%H:%M")
print("date and time =", dt_string)	

def generateDates (tripDates ):
    raise NotImplementedError


record = {
    'recordedTime' : 'Slavko' 
}
