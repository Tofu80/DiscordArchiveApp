#!/usr/bin/env python3

import requests
import json 

TOKEN = "MjU4MjA5OTY3OTg1Nzg2ODgx.Gv3rD_.KIvMW4vHhLLNWiJR6zkY1LCxwyoktG5jDjKDF4"

headers = {
    "Authorization": TOKEN 
}

def getMyProfile():
    response = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
    data = response.json()
    print(json.dumps(data, indent=2))

def getDms():
    response = requests.get("https://discord.com/api/v10/users/@me/channels", headers=headers)
    data = response.json()
    print(json.dumps(data, indent=2))

def getMessages(channelId, limit=100):
    url = f"https://discord.com/api/v10/channels/{channelId}/messages?limit={limit}"
    response = requests.get(url, headers=headers)
    data = response.json()

    print(json.dumps(data, indent=2))
    
    # for message in data: 
    #     author = message["author"]["username"]
    #     timestamp = message["timestamp"]
    #     content = message["content"]
    #     print(f"[{timestamp}] {author}: {content}")


# print("===MY PROFILE===")
# getMyProfile()

# print("===MY DMS===")
# getDms()

getMessages("578889592317673485")

