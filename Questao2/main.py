import requests

url = 'https://viacep.com.br/ws/'
cep_principal = 30140071

for i in range(5):
    cep = str(cep_principal + i)
    formato = '/xml/'

    r = requests.get(url + cep + formato)
    if (r.status_code == 200):
        print('CEP:' , cep)
        print('XML : ', r.text)
        print()
    else:
        print('Nao houve sucesso na requisicao.')