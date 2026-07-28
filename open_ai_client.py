from config import OPEN_AI_KEY
from openai import OpenAI

def aiProcess(command):
    client = OpenAI(
    api_key=  OPEN_AI_KEY,
    base_url="https://openrouter.ai/api/v1"
    )

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",  # change this to your OpenRouter model
        # model="openrouter/gpt-oss-20b:free",
        messages=[
            {
                "role": "system",
                "content":"You area virtual assistant name jarvis skilled in tasks like Alexa"
            },
            {
                "role": "user",
                "content": command
            }
            
        ]
    )

    reply = response.choices[0].message.content
    print(reply)
    return reply