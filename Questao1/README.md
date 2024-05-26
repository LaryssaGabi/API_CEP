# Atividade 1

```bash

import requests
import xml.etree.ElementTree as ET

url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'

r = requests.get(url + cep + formato)

if r.status_code == 200:

    root = ET.fromstring(r.content)
    

    def print_xml(element, level=0):
        indent = "  " * level
        print(f"{indent}<{element.tag}>")
        if element.text:
            print(f"{indent}  {element.text}")
        for child in element:
            print_xml(child, level + 1)
        print(f"{indent}</{element.tag}>")
    
    print()
    print('XML : ')
    print_xml(root)
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

* import requests: Importa a biblioteca requests, que é utilizada para fazer requisições HTTP.
* import xml.etree.ElementTree as ET: Importa o módulo ElementTree da biblioteca padrão xml, que é utilizado para analisar e manipular dados XML.


* url = 'https://viacep.com.br/ws/': Define a URL do serviço de consulta de CEP.
* cep = '30140071': Define o CEP que será consultado.
* formato = '/xml/': Define o formato de resposta do serviço, que é XML. "O qual a professora solicitou"

* r = requests.get(url + cep + formato): Faz uma requisição GET para a URL definida, passando o CEP e o formato de resposta como parâmetros. A resposta é armazenada na variável r.

* if r.status_code == 200: Verifica se a requisição foi bem-sucedida, com código de status 200.

* root = ET.fromstring(r.content): Converte o conteúdo da resposta em uma árvore XML, usando o módulo ElementTree 

* def print_xml(element, level=0): Define uma função para imprimir a estrutura da árvore XML

* Caso a consulta não tenha um resultado de sucesso, irá terminhas informando "Nao houve sucesso na requisicao."

----------------------------------------------------------------------------------------

# Atividade 2

``` bash
import requests
import xml.etree.ElementTree as ET

def get_address_info(cep):
    url = 'https://viacep.com.br/ws/'
    formato = '/xml/'

    r = requests.get(url + cep + formato)

    if r.status_code == 200:
        # Parsing the XML response
        root = ET.fromstring(r.content)
        
        # Pretty print the XML response
        def print_xml(element, level=0):
            indent = "  " * level
            print(f"{indent}<{element.tag}>")
            if element.text:
                print(f"{indent}  {element.text.strip()}")
            for child in element:
                print_xml(child, level + 1)
            print(f"{indent}</{element.tag}>")
        
        print('XML : ')
        print_xml(root)
    else:
        print('Nao houve sucesso na requisicao.')

if __name__ == "__main__":
    base_cep = 30140071
    for i in range(5):
        cep = str(base_cep + i)
        print(f"Consultando CEP: {cep}")
        get_address_info(cep)
        print("\n" + "="*40 + "\n")


```