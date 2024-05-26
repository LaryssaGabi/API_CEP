import requests

url = 'https://viacep.com.br/ws/'
uf = 'MG'
city = 'Contagem'
endereco = 'Rua Maria Olinda Nascimento'
formato = '/xml/'

r = requests.get(url + uf + '/' + city + '/' + endereco + formato)
if (r.status_code == 200):
    print('Endereco: ', endereco)
    print('XML : ', r.text)
    print()
else:
    print('Nao houve sucesso na requisicao.')