import requests
import json

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
#print(response)
#print(response.json())
if response.status_code == 200:
    for news_id in response.json():
        get_news = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{news_id}.json')
        title = get_news.json()['title']
        print(title)
else:
    print('Error connecting')