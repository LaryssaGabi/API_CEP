# Atividade 1

``` bash

import requests
url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/json/'
r = requests.get(url + cep + formato)
if (r.status_code == 200):
print()
print('JSON : ', r.json())
print()
else:
print('Nao houve sucesso na requisicao.')

```

### Alteração

```bash

import requests

url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'  # Alterado para XML

r = requests.get(url + cep + formato)

if r.status_code == 200:
    print()
    print('XML :', r.text)  # Use r.text para obter a resposta em XML
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
 python main.py

```

----------------------------------------------------------------------------------------
