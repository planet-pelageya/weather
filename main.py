import requests

cities = ["Лондон","Череповец", "Шереметьево"]
payload ={"lang":"ru","n":'',"T":'',"q":'',"M":''}

def temperature(*args):
    for i in cities:
        r = requests.get(f"https://wttr.in/{i}", params=payload)
        r.raise_for_status()
        print(r.text)

if __name__ == '__main__':
    temperature(cities)
