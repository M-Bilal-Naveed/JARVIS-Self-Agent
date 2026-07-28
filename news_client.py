import requests
from config import NEWS_API_KEY, NEWS_API_URL

def get_news():
    params = {
        "country": "us",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_API_URL, params=params)

    print(response.status_code)
    print(response.json())   # <-- Add this

    data = response.json()

    # return data["articles"]
    if data.get("status") == "ok":
       return data.get("articles", [])

    print(data)
    return []