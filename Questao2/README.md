# Atividade 2

``` bash
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
 python main.py

```

### Explicando a Atividade

* Foi adicionado um For que seria uma repetição com o range para seguir a sequendia da adição das númerações no CEP.
* Foi adicionado um if para verificar se a requisição foi bem sucedida.
* Foi utilizdao também o str para converte o numero do CEP em string para fazer a manipulação dele



----------------------------------------------------------------------------------------

