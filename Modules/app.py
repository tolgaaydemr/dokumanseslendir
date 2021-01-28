from pprint import pprint
import webbrowser
from Modules.speech_Recognition import speak
import os
import requests


def search():
    # speak()   parametre gelecek
    firefox_path = '/usr/bin/firefox'
    url = 'https://www.google.com/'
    webbrowser.get(firefox_path).open(url)


def music():
    speak()
    spotify_path = '/snap/bin/spotify'
    os.system(spotify_path)


def weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ebe2061248108e50b0664f94b5d1cf27'.format(city)
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    x = round(temp-273, 0)
    return x
    # print('Temp: {:3.0f} degree'.format(x))
