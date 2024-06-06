import requests


def main():
    get_temperature()

def get_temperature():
    cities = ["Лондон", "Череповец", "Шереметьево"]
    payload ={"lang":"ru","n":'',"T":'',"q":'',"M":''}
    for i in cities:
        r = requests.get(f"https://wttr.in/{i}", params=payload)
        r.raise_for_status()
        print(r.text)


if __name__ == '__main__':
    main()
