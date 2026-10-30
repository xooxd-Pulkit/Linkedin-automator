from google import genai
from dotenv import load_dotenv

load_dotenv("key.env")
client=genai.Client()
response=client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Explain Python",
    # max_output_tokens=150
)
print(response.text)
with open("./draft.txt","w") as file:
    file.write(response.text)
