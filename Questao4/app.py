import requests

url = 'https://viacep.com.br/ws/'

r = requests.get(url)

print("Status retorno: ", r.status_code)
print('TEXT : ', r.text)
