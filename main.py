import requests 
payload ={"lang":"ru","n":'',"T":'',"q":'',"M":''} 
result = requests.get("https://wttr.in/Череповец",params = payload) 

print(result.text)