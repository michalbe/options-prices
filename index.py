import re

def get_price(symbol):
    ticker = re.findall(r'[a-zA-Z]+', symbol)[0]
    print(ticker)


get_price("IPOF210416C00022500")
