import requests
import json
from gpiozero import Button
from time import sleep
import datetime
# generate random Gaussian values
from random import seed
from random import randint

def log():
    # create a new event - replace with your API
    # url = 'https://modas.azurewebsites.net/api/event/'
    url = 'https://modas-jsg.azurewebsites.net/api/event'
    headers = { 'Content-Type': 'application/json'}
    t = datetime.datetime.now()
    t_json = "{0}-{1}-{2}T{3}:{4}:{5}".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"), t.strftime("%H"), t.strftime("%M"), t.strftime("%S"))
    d_string = "{0}-{1}-{2}".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"))
    # seed random number generator
    # seed(1)         
    # generate some integers
    location = randint(1, 3)
    print(location)
    flag = False
    payload = { 'timestamp': t_json, 'flagged': flag, 'locationId': location }
    # post the event
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(r.status_code)
    print(r.json())
    filename = d_string + ".log"
    f = open(filename, "a")
    f.write(t_json + "," + str(flag) + "," + str(location) + "," + str(r.status_code) + "\n")
    f.close()
    
    
# init button
button = Button(8)
button.when_released = log

try:
    # program loop
    while True:
        sleep(.001)
# detect Ctlr+C
except KeyboardInterrupt:
    print("goodbye")