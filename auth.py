import os
import webbrowser
import requests
import secrets
from dotenv import load_dotenv
from urllib.parse import quote

def auth():

    load_dotenv("key.env")
    client_id = os.getenv("LINKEDIN_CLIENT_ID")
    client_secret = os.getenv("LINKEDIN_CLIENT_SECRET")
    redirect_url="http://localhost:8000/callback"
    # print(quote(redirect_url,safe=""))
    auth_url=f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={client_id}&redirect_uri={quote(redirect_url, safe='')}&scope=w_member_social"
    print(auth_url)
    webbrowser.open(auth_url)