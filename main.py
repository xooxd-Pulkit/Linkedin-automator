from google import genai
from dotenv import load_dotenv
import os
load_dotenv("key.env")
client=genai.Client()
files_uploaded=[]
sub_uploaded=[]
count=1
def file_uploader(path,sub):
    # while(count==1):
        try:
            with os.scandir(path) as folder:
                for entry in folder:
                    # print(entry.name)
                    if(entry.is_file()):
                        upload_file=client.files.upload(file=entry.path)
                        print(upload_file.uri)
                        # count=2
                        if(sub):
                            sub_uploaded.append(upload_file)
                        else:
                            files_uploaded.append(upload_file)
                    elif(entry.is_dir()):
                        file_uploader(entry.path,True)
                        files_uploaded.append(sub_uploaded)
                        sub_uploaded=[]
        except FileNotFoundError:
            print(f"The directory {path} was not found.")

file_uploader("D:/Pulkit/100 days python/Day 24",False)


response=client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=f"{files_uploaded} summarize these file content in 50 words",
    # max_output_tokens=150
)
print(response.text)
with open("./draft.txt","w") as f:
    # f.write(response.text)
    pass

def promp_gen():
    client=genai.Client()
    response=client.models.generate_content(model="gemini-3.1-flash-lite",contents="")
