import pyperclip
import sys
import time
import requests
import json
from datetime import datetime

clipfileloc = "/mnt/c/syno/cliper/"
room = "!XExxxxxxx:my.matrix.host"
url = "https://matrix.x.xyz/_matrix/client/r0/rooms/"+room+"/send/m.room.message"
atoken = "XXxxY2xvY2F0aW9uxxxxxxxxxxxxxxxxx"

def matrix(fbody):
    print (json.dumps(fbody))
    querystring = {"access_token":atoken}
    payload = "{\n\"msgtype\": \"m.text\",\n\"format\": \"org.matrix.custom.html\",\n\"formatted_body\":"+json.dumps(fbody)+",\n\"body\": \"bbody\"\n}"
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

def monitor():
    clip = ""
    file_name = "log.txt"
    counter = 0
    while True:
        try:
            if clip != pyperclip.paste():
                clip = pyperclip.paste()
                print (clip)
                matrix(clip)
                counter += 1
                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d %H.%M.%S.txt")
                #print("Current Time =", current_time)
                file = open(clipfileloc+current_time, "a")  # instead w a for  append
                file.write(clip + "\n")
                file.close()
            time.sleep(1.2)
        except KeyboardInterrupt:
            print ("by by")
            sys.exit()
try:
    monitor()
except Exception as e:
    print (e)
