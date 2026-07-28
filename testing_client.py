import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini"
    messages=[
        {
            "role": "system",
            "content":"You area virtual assistant name jarvis skilled in tasks like Alexa"
        },
        {
            "role": "user",
            "content":"Compose a poem that explain the concept of recursion in programming"
        }
        
    ]
)

print(response.choices[0].message.content)