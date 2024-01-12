**Conversor de Moedas API**

*Descrição*

Esta API fornece um serviço de conversão de moedas em tempo real, suportando várias moedas, incluindo USD, BRL, EUR, BTC e ETH. A API utiliza a CryptoCompare para obter cotações atualizadas e realiza conversões monetárias com base nos valores mais recentes.

**Pré-requisitos**

Docker
Git

**Como Executar**

1 - Clone o repositório:

git clone [URL do seu repositório]

2- Navegue até o diretório do projeto:

cd [nome do seu diretório]

3- Construa a imagem Docker:

docker build -t conversao-monetaria .

4- Execute a aplicação:

docker run -p 5000:5000 conversao-monetaria

A API agora estará acessível em localhost:5000/convert.

**Uso**

Para realizar uma conversão, faça uma requisição GET com os seguintes parâmetros:

from: Moeda de origem (ex: BTC)
to: Moeda de destino (ex: EUR)
amount: Valor a ser convertido (ex: 123.45)

Exemplo de requisição:

http://localhost:5000/convert?from=BTC&to=EUR&amount=123.45