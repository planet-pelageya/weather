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
