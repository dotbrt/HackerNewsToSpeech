import pyttsx3
from bs4 import BeautifulSoup as bs
import requests
import time
html = requests.get('https://news.ycombinator.com/')
soup = bs(html.content, 'html.parser')
engine  = pyttsx3.init()
for a in soup.find_all('a', class_="storylink"):
    try:
        print(a.text)
        time.sleep(1)
        engine.say(a.text)
        engine.runAndWait()
    except KeyboardInterrupt:
        href = a.get('href')
        follow = requests.get(href)
        new_soup = bs(follow.content, 'html.parser')
        print(new_soup.find('article'))
        break
