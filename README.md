# README - Consultas com ViaCEP

Este projeto consiste em realizar consultas utilizando a API do ViaCEP. As instruções das perguntas estão detalhadas no arquivo [api_cep.pdf](./api_cep.pdf). Abaixo estão as perguntas que devem ser abordadas:

## Perguntas

### Questão 1
Modifique o seguinte código para retornar a resposta da requisição "GET" em formato XML:
```python
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

### Questão 2
Modifique o código anterior para que, usando uma estrutura de repetição, consulte 5 CEPs sequenciais.  
Suponha que o CEP da sua casa seja 30140-071, o código Python deverá enviar 5 requisições com os seguintes CEPs:  
30140071, 30140072, 30140073, 30140074 e 30140075.  
O resultado deve ser exibido na tela.

### Questão 3
Modifique o código para que a consulta seja feita com um endereço (nome de rua), ao invés do CEP.  
Veja a URL de exemplo:  
`viacep.com.br/ws/MG/Belo Horizonte/Rua dos Aimores/json/`

### Questão 4
Modifique o primeiro código de tal forma que o endereço `https://viacep.com.br/abc/` tente ser acessado. Exiba o código de retorno e o texto.
