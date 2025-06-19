import requests, json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_trending(region='IN', max_results=50):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode={region}&maxResults={max_results}&key={API_KEY}"
    res = requests.get(url)
    data = res.json()

    # 🔧 Create data/ folder if it doesn't exist
    os.makedirs('data', exist_ok=True)

    with open('D:/Sharanya/You tube Trend Analyser/data/trending_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("Data saved to data/trending_data.json")

fetch_trending('IN')
