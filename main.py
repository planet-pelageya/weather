import requests

cities = ["Лондон","Череповец", "Шереметьево"]
#я оставил переменную выше шлобальной, чтобы если что можно было поменять города

def get_temperature():
    payload ={"lang":"ru","n":'',"T":'',"q":'',"M":''}
    for i in cities:
        r = requests.get(f"https://wttr.in/{i}", params=payload)
        r.raise_for_status()
        print(r.text)

get_temperature()
