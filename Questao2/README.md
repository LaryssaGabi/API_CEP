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



----------------------------------------------------------------------------------------

