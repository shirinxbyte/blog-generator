import os
from openai import OpenAI
from dotenv import load_dotenv

# Lade Umgebungsvariablen
load_dotenv()

# Zugriff auf API-Key
api_key = os.getenv("OPENAI_API_KEY")

# Erstelle Client
client = OpenAI(api_key=api_key)

# Funktion zum Generieren eines Absatzes
def generate_blog(paragraph_topic):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who writes blog paragraphs."},
            {"role": "user", "content": f"Write a paragraph about the following topic: {paragraph_topic}"}
        ],
        max_tokens=400,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# Eingabeschleife
keep_writing = True

while keep_writing:
    answer = input("Write a paragraph? (Y = yes, anything else = no): ")
    if answer.upper() == "Y":
        paragraph_topic = input("What should this paragraph talk about? ")
        print("\n" + generate_blog(paragraph_topic))
        print("\n---\n")
    else:
        keep_writing = False
        print("Goodbye!")
