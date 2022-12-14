<h1 align="center"> Desafio Confitec</h1>

## Descrição do projeto 

<p align="justify">
Projeto desenvolvido em cima do que foi pedido no desafio.

A integração das ferramentas da AWS foi feita da seguinte forma:


![esquema_aws](https://user-images.githubusercontent.com/69823706/192107348-b42ee4ad-515a-4b87-b8cf-afe12dd9a34c.png)
</p>

## Passo a passo para a execução da aplicação

Requisitos: 
Python,
Redis

1° Passo - Clonar o repositorio em uma pasta de sua preferência.
```git clone url_repositorio```

2° Passo - Instalar as bibliotecas necessarias para a execução da aplicação.
```pip install -r requirements.txt```

3° Passo - Executar o app.py que iniciará a API
```python app.py```

4° Passo - Utilizar algum software como o "Postman" para fazer as requisições na API.

5° Passo - Para interagir basta chamar a API pela URL e passar os parâmetros:
Exemplo: 
```http://0.0.0.0:5000/artist/16775?cache=True```


## O Desafio 

:heavy_check_mark: `Parte 1:` Criar uma API REST em Python (FLASK) que consuma a API do Genius 
(Documentação no link abaixo) que dado um artista liste as 10 músicas mais populares 
do artista pesquisado, salve um id de transação no formato uuid versão 4 e o nome do 
artista pesquisado em uma coleção no DynamoDB, os dados de retorno da 
consulta à API devem ser salvos no Redis por 7 dias.

:heavy_check_mark: `Parte 2:` Ao buscar um artista pela API, verificar se existe uma transação salva e se a mesma 
ainda encontra-se disponível em cache (Redis), caso existente, enviar os dados do Redis, 
caso contrário, seguir o informado na etapa 1.

:heavy_check_mark: `Parte 3:` A consulta deverá permitir a passagem via query string, que é a opção de manter os dados 
em cache, caso enviado o parâmetro "cache=False" limpe a transação do Redis e 
atualize o DynamoDB com a opção de escolhida pelo usuário, o não envio do 
parâmetro indica que deve-se utilizar os dados em cache.

:heavy_check_mark: `Parte 4:` Envie o link do github com o código fonte do projeto junto com um "README" com 
um passo à passo para a execução da aplicação.
