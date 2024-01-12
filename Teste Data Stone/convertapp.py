from flask import Flask, request, jsonify, abort
import requests
from config import API_KEY
import logging

# Gravar logs app.log
logging.basicConfig(filename='app.log',filemode='a', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert():
    # Obtendo parâmetros
    from_currency = request.args.get('from').upper()
    to_currency = request.args.get('to').upper()
    amount = request.args.get('amount')

    # validação de existencia das principais moedas.
    supported_currencies = ['USD', 'BRL', 'EUR', 'BTC', 'ETH']
    if from_currency not in supported_currencies or to_currency not in supported_currencies:
        return jsonify({"erro": "Moeda não suportada"}), 400
    
    # Validações dos parametros obrigatorios
    if not all([from_currency, to_currency, amount]):
        logging.error("Parâmetros insuficientes'")
        abort(400, description="Parâmetros insuficientes")

    # validação do valor para a conversao.
    try:
        amount = float(amount)
    except ValueError:
        logging.error("Valor inválido para 'amount'")
        abort(400, description="Valor inválido para 'amount'")


    # Conversao do valor do parametro 'from_currency' para a moeda lastro.        
    if from_currency != 'USD':
        url_to_usd = f'https://min-api.cryptocompare.com/data/price?fsym={from_currency}&tsyms=USD&api_key={API_KEY}'
        response_to_usd = requests.get(url_to_usd)
        if response_to_usd.status_code != 200:
            logging.error("Erro na conversão para USD")
            return jsonify({"erro": "Erro na conversão para USD"}), 500
        data_to_usd = response_to_usd.json()
        rate_to_usd = data_to_usd['USD']
        amount_in_usd = amount * rate_to_usd
    else:
        amount_in_usd = amount

    #Conversão do valor do parametro 'to_currency para moeda lastro
    if to_currency != 'USD':
        url_from_usd = f'https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms={to_currency}&api_key={API_KEY}'
        response_from_usd = requests.get(url_from_usd)
        if response_from_usd.status_code != 200:
            logging.error("Erro na conversão para USD")
            return jsonify({"error": "Erro na conversão de USD"}), 500
        data_from_usd = response_from_usd.json()
        rate_from_usd = data_from_usd[to_currency]
        converted_amount = amount_in_usd * rate_from_usd
    else:
        converted_amount = amount_in_usd

    logging.info(f'Conversão realizada de {from_currency} para {to_currency}')
    
    conversion_rate = round(converted_amount / amount, 2)
    converted_amount = round(converted_amount, 2)
    # Retorno da conversao.
    return jsonify({
        'conversao_de': from_currency,
        'conversao_para': to_currency,
        'valor_original': amount,
        'valor_convertido': converted_amount,
        'taxa_de_coneversao': conversion_rate,
        'mensagem': f'{amount} {from_currency} foram convertidos para {converted_amount} {to_currency} usando uma taxa de conversao de {conversion_rate}.'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
