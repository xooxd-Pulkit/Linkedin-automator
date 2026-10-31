from google import genai
from dotenv import load_dotenv
from configparser import ConfigParser
import os
import requests
load_dotenv("key.env")
config = ConfigParser()
config.read("codes.ini")

# client=genai.Client()
# files_uploaded=[]
# sub_uploaded=[]

# with open("./promp.txt","r") as f:
#     prompt=f.read()
# def file_uploader(path,sub):
#     # while(count==1):
#     global sub_uploaded
#     try:
#         with os.scandir(path) as folder:
#             for entry in folder:
#                 # print(entry.name)
#                 if(entry.is_file()):
#                     upload_file=client.files.upload(file=entry.path)
#                     print(upload_file.uri)
#                     # count=2
#                     if(sub):
#                         sub_uploaded.append(upload_file)
#                     else:
#                         files_uploaded.append(upload_file)
#                 elif(entry.is_dir()):
#                     file_uploader(entry.path,True)
#                     files_uploaded.append(sub_uploaded)
#                     sub_uploaded=[]
#     except FileNotFoundError:
#         print(f"The directory {path} was not found.")
# with open("./day.txt","r+") as file:
#     day_counter=int(file.read())
#     print(type(day_counter))
#     file_uploader(f"D:/Pulkit/100 days python/Day {day_counter}",False)
#     day_counter=day_counter+1
#     file.seek(0)
#     file.write(str(day_counter))

# # print(files_uploaded)

# response=client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=f"""{files_uploaded}{prompt}{day_counter-1}."""
#     # max_output_tokens=150
# )
# # print(response.text)
# with open("./draft.txt","w") as f:
#     f.write(response.text)

url = "https://api.linkedin.com/rest/posts"
post_data=data = {
    "author": f"urn:li:person:{config['LINKEDIN']['member_sub']}",
    "commentary": "Hello LinkedIn! This 2nd post was created using Python API. #Python #Automation",
    "visibility": "PUBLIC",
    "distribution": {
        "feedDistribution": "MAIN_FEED",
        "targetEntities": [],
        "thirdPartyDistributionChannels": []
    },
    "lifecycleState": "PUBLISHED",
    "isReshareDisabledByAuthor": False
}
headers = {
    "Authorization": f"Bearer {config['LINKEDIN']['access_token']}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0",
    "LinkedIn-Version": "202610"
}
response=requests.post(url,headers=headers,json=post_data)
# data=response.json()
print("Status:", response.status_code)
print("Response:", response.text)
print("Post ID:", response.headers.get("x-restli-id"))


# import requests

# Use your existing headers with the access token
# import requests

# headers = {
#     "Authorization": f"Bearer {config['LINKEDIN']['access_token']}"
# }

# # Standard OpenID Connect endpoint for user details
# response = requests.get("https://api.linkedin.com/v2/userinfo", headers=headers)
# print(response.json())