from google import genai
from dotenv import load_dotenv
import os

load_dotenv("key.env")

client=genai.Client()
files_uploaded=[]
sub_uploaded=[]

with open("./promp.txt","r") as f:
    prompt=f.read()
def file_uploader(path,sub):
    # while(count==1):
    global sub_uploaded
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
with open("./day.txt","r+") as file:
    day_counter=int(file.read())
    print(type(day_counter))
    file_uploader(f"D:/Pulkit/100 days python/Day {day_counter}",False)
    day_counter=day_counter+1
    file.seek(0)
    file.write(str(day_counter))

# print(files_uploaded)

response=client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=f"""{files_uploaded}{prompt}{day_counter-1}."""
    # max_output_tokens=150
)
# print(response.text)
with open("./draft.txt","w") as f:
    f.write(response.text)
    

def promp_gen():
    client=genai.Client()
    response=client.models.generate_content(model="gemini-3.1-flash-lite",contents="")
