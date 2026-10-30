from google import genai
from dotenv import load_dotenv
import os
load_dotenv("key.env")
def sub_folder(path):
    with os.scandir(path) as sub:
        for entry in sub:
            print(entry.name)
            if(entry.is_dir()):
                sub_folder(entry.path)
# with os.scandir("D:/Pulkit/100 days python/Day 24")as folder:
#     for entry in folder:
#         print(entry.name)
#         if(entry.is_dir()):
#             sub_folder(entry.path)
sub_folder("D:/Pulkit/100 days python/Day 24")


client=genai.Client()
response=client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Explain Python",
    # max_output_tokens=150
)
print(response.text)

def promp_gen():
    client=genai.Client()
    response=client.models.generate_content(model="gemini-3.1-flash-lite",contents="")
