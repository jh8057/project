import requests

payload = {'data': 'hello'}

a = requests.get('http://127.0.0.1:5000/sample_restapi', params=payload)
print(a.text)
