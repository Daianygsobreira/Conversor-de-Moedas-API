# Conversor-de-Moedas-API

Desafio Técnico desenvolvedor backend Python/Django

Construa uma API, que responda JSON, para conversão monetária. Ela deve ter uma
moeda de lastro (USD) e fazer conversões entre diferentes moedas com cotações de
verdade e atuais.

A API deve, originalmente, converter entre as seguintes moedas:

USD

BRL

EUR

BTC

ETH

Ex: USD para BRL, USD para BTC, ETH para BRL, etc...

A requisição deve receber como parâmetros: A moeda de origem, o valor a ser
convertido e a moeda final.

Ex: ?from=BTC&to=EUR&amount=123.45

Requisitos

O código precisa rodar em Linux Ubuntu (preferencialmente como container Docker)
Para executar seu código, deve ser preciso apenas rodar os seguintes comandos:

git clone $seu-fork
cd $seu-fork
comando para instalar dependências
comando para executar a aplicação

A API pode ser escrita com ou sem a ajuda de frameworks (À sua escolha)

# Solução
___________________________________________________________________________________________________________________________________________________________________________________________________

No desenvolvimento em Python, usei Flask para Criar a rota de chamada da API,request para consumir a API da Cryptocompare,e unittest para os testes unitarios, para resolver o problema proposto. A arquitetura é orientada a serviços, focada em fornecer um serviço de API para conversão de moedas.

A estrutura de pastas da aplicação é:

- convertapp.py
Código principal que define os endpoints da API e a lógica de negócios.
- dockerfile
Configura o ambiente de execução da aplicação, encapsulando as dependências e facilitando a implantação.
- requirements.txt
Lista as dependências necessárias, permitindo fácil instalação em ambientes diferentes.
- config.py
Usado para configurações (como chaves de API), separando as configurações do código principal.
-test_api.py
Os testes unitarios foram feitos seguindo boas práticas de desenvolvimento para garantir a funcionalidade do código.

Testes unitários

Foi utilizado o unitteste, para executá-los rode  python test_api.py

# Pré-requisitos

Docker
Git

 # Como Executar

1 - Clone o repositório:

git clone https://github.com/Daianygsobreira/Conversor-de-Moedas-API.git

2- Navegue até o diretório do projeto:

cd Teste Data Stone 

3- Construa a imagem Docker:

docker build -t conversao-monetaria .

4- Execute a aplicação:

docker run -p 5000:5000 conversao-monetaria

A API agora estará acessível em localhost:5000/convert.

# Uso

Para realizar uma conversão, faça uma requisição GET com os seguintes parâmetros:

from: Moeda de origem (ex: BTC)

to: Moeda de destino (ex: EUR)

amount: Valor a ser convertido (ex: 123.45)

Exemplo de requisição:

http://localhost:5000/convert?from=BTC&to=EUR&amount=123.45


Retornará um objeto com as informações:

{
  "conversao_de": "BTC",

  "conversao_para": "EUR",
  
  "mensagem": "123.45 BTC foram convertidos para 4920449.71 EUR usando uma taxa de conversao de 39857.83.",
  
  "taxa_de_coneversao": 39857.83,
  
  "valor_convertido": 4920449.71,
  
  "valor_original": 123.45
  
}

# Requisitos

O código precisa rodar em Linux Ubuntu (preferencialmente como container Docker)
Para executar seu código, deve ser preciso apenas rodar os seguintes comandos:

git clone $seu-fork
cd $seu-fork

comando para instalar dependências
comando para executar a aplicação

A API pode ser escrita com ou sem a ajuda de frameworks (À sua escolha)

Critérios de avaliação

Organização do código: Separação de módulos, view e model, back-end e front-end

Clareza: O README explica de forma resumida qual é o problema e como pode rodar
a aplicação?

Assertividade: A aplicação está fazendo o que é esperado? Se tem algo faltando, o

README explica o porquê?

Legibilidade do código (incluindo comentários)

Segurança: Existe alguma vulnerabilidade clara?

Cobertura de testes (Não esperamos cobertura completa)

Histórico de commits (estrutura e qualidade)

Escolhas técnicas: A escolha das bibliotecas, banco de dados, arquitetura, etc, é a

melhor escolha para a aplicação?

Entrega

Pode ser o link para um repositório público (github, bitbucket, gitlab), um repositório
privado (nos enviando um convite para visualizar) ou, em último caso um zip com o
repositório (lembrar de manter a pasta .git no repositório).
