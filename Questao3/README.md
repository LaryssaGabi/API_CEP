# Atividade 3

``` bash
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

```

### Intalar as dependencias

``` bash
 python -m venv venv

```

``` bash
 .\venv\Scripts\activate

```

``` bash
 pip install -r requirements.txt

```

``` bash
 python app.py

```

----------------------------------------------------------------------------------------

