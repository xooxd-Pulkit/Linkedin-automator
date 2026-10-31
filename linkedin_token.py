import requests
from configparser import ConfigParser
from dotenv import load_dotenv
import os
load_dotenv("key.env")
print(os.getenv("LINKEDIN_CLIENT_ID"))
# os.getenv("LINKEDIN_CLIENT_SECRET")
# config=ConfigParser()
# config.read("codes.ini")

# url = "https://www.linkedin.com/oauth/v2/accessToken"
# data = {
#     "grant_type": "authorization_code",
#     "code": config["LINKEDIN"]["access_code"],
#     "client_id": CLIENT_ID,
#     "client_secret": CLIENT_SECRET,
#     "redirect_uri": REDIRECT_URI
# }
# response=requests.post(url,data=data)