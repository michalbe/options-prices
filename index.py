import re
from yahooquery import Ticker
from datetime import datetime

now = datetime.now()
rows = []

local_path = './'
# local_path = '/var/www/options/'

def get_price(symbol):
    ticker = re.findall(r'[a-zA-Z]+', symbol)[0]

    yahoo_data = Ticker(ticker)
    price = yahoo_data.option_chain.query('`contractSymbol` == "' + symbol +'"')["lastPrice"][0]
    return price


def main():
    with open(local_path + 'template.html', 'r') as file:
        template = file.read()

    with open(local_path + 'row_template.html', 'r') as file:
        row_template = file.read()

    symbol_list = open(local_path + 'symbols.txt', 'r')

    for symbol in symbol_list:
        symbol = symbol.strip()
        price = get_price(symbol)
        rows.append(row_template % {'label': symbol, 'value': price})

    output = template % {
        'content': '\n'.join(rows),
        'update_time': now.strftime("%d/%m/%Y %H:%M:%S")
    }

    print(output)

main()
