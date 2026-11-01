import requests
from configparser import ConfigParser
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv("key.env")
client_id=os.getenv("LINKEDIN_CLIENT_ID")
client_sec=os.getenv("LINKEDIN_CLIENT_SECRET")
config=ConfigParser()
config.read("codes.ini")
current_seconds = int(datetime.now().timestamp())
# print(type(int_seconds))  

url = "https://www.linkedin.com/oauth/v2/accessToken"
data = {
    "grant_type": "authorization_code",
    "code": config["LINKEDIN"]["access_code"],
    "client_id": client_id,
    "client_secret": client_sec,
    "redirect_uri": "http://localhost:8000/callback"
}
def linkedin_token():

    response=requests.post(url,data=data)
    data=response.json()
    token=data["access_token"]
    config["LINKEDIN"]["access_token"]=token
    config["LINKEDIN"]["expiry_sec"]=str(current_seconds+5000000)
    with open("codes.ini","w") as f:
        config.write(f)

    print(data)


# response = requests.get(
#     "https://api.linkedin.com/v2/userinfo",
#     headers={"Authorization": f"Bearer {config["LINKEDIN"]["access_token"]}"}
# )
# data=response.json()
# # print(response.json())
# print(data["scope"])