import requests

cities = ["Лондон","Череповец", "Шереметьево"]
payload ={"lang":"ru","n":'',"T":'',"q":'',"M":''}

def temperature(*args):
    for i in cities:
        try:
            r = requests.get(f"https://wttr.in/{i}", params=payload)
            print(r.text)
        except:
            return None

if __name__ == '__main__':
    temperature(cities)

# Это мой готовый вариант. При нём у меня не выскакивает куча красного текста и ошибок, ниже укажу как я понял нужно работать с raise_for_status() и status.code
_________________________________________________________________________________
import requests

cities = ["Лондон","Череповец", "Шереметьево"]
payload ={"lang":"ru","n":'',"T":'',"q":'',"M":''}

def temperature(*args):
    for i in cities:
        r = requests.get(f"https://wttr.in/{i}", params=payload)
        if r.status_code == 200:
            print(r.text)
        else:
            return None

if __name__ == '__main__':
    temperature(cities)
___________________________________________________________________________

import requests

cities = ["Лондон","Череповец", "Шереметьево"]
payload ={"lang":"ru","n":'',"T":'',"q":'',"M":''}

def temperature(*args):
    for i in cities:
        try:
            r = requests.get(f"https://wttr.in/{i}", params=payload)
            r.raise_for_status()
            print(r.text)
        except:
            None

if __name__ == '__main__':
    temperature(cities)
