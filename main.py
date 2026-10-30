from google import genai
from dotenv import load_dotenv
import os
load_dotenv("key.env")
client=genai.Client()
files_uploaded=[]
sub_uploaded=[]


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
    contents=f"""{files_uploaded}Analyze all the files provided to you carefully. They contain my work, code, notes, exercises, and projects from a particular day of my 100 Days of Python journey.

Understand the actual work I have completed and identify:

- What Python concepts and technical skills I learned.
- What I practically implemented and experimented with.
- What programs, exercises, or projects I developed and their functionality.
- What new programming techniques, modules, libraries, or methods I used.
- What challenges I encountered and what problem-solving skills I demonstrated.
- What meaningful progress I made as a Python developer.

Connect related files and understand the complete context instead of analyzing each file independently.

Now, act as an experienced software engineer and professional LinkedIn content strategist. Based on your analysis, write ONE polished, engaging, ready-to-publish LinkedIn post in first person, as if I wrote it myself.

**Writing requirements:**
- Start with a strong, natural hook.
- Clearly communicate what I learned and built.
- Highlight practical implementations rather than simply listing concepts.
- Explain interesting technical aspects without making the post unnecessarily lengthy.
- Maintain a professional, authentic, conversational tone.
- Make it engaging for developers, recruiters, and fellow learners.
- Use natural English appropriate for a Computer Science student.
- Include relevant emojis sparingly.
- End with a meaningful reflection or engaging question.
- Add 4–6 relevant hashtags.

**Strict rules:**
- Never invent achievements, projects, features, or learning outcomes.
- Never exaggerate simple exercises into major accomplishments.
- Distinguish between concepts studied and concepts actually implemented.
- Do not repeat information or use generic motivational statements.
- Never include API keys, passwords, credentials, or sensitive information.
- If information is unclear, do not make assumptions.

The post should demonstrate genuine technical progress, not pretend expertise.

**Output only the final LinkedIn post.** Do not provide file analysis, explanations, suggestions, multiple versions, or any introductory commentary.

Before responding, verify technical accuracy, authenticity, readability, and factual consistency with the supplied files. Make the final post ready to copy and publish without editing. Also mention day number in the post day is {day_counter-1}."""
    # max_output_tokens=150
)
# print(response.text)
with open("./draft.txt","w") as f:
    f.write(response.text)
    

def promp_gen():
    client=genai.Client()
    response=client.models.generate_content(model="gemini-3.1-flash-lite",contents="")
