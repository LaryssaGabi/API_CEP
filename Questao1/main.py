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