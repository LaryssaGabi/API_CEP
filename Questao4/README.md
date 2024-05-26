# Atividade 4

``` bash
import requests

url = 'https://viacep.com.br/ws/'

r = requests.get(url)

print("Status retorno: ", r.status_code)
print('TEXT : ', r.text)

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

### Explicando a Atividade

* Requests permite enviar solicitações HTTP facilmente.
* Url solicitada pela professora para verificar
* Utilizado a rota do get para mostrar tudo da pagina
* O retono do status de 404 que vai aparecer
* E a formatação text será os estilos, e o html da pagina que vai aparecer no terminal, detalhadamente

----------------------------------------------------------------------------------------

