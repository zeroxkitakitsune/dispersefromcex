import ccxt
from ccxt.base.errors import InvalidAddress, InvalidOrder, ExchangeError
from termcolor import cprint
import time
import json

KUCOIN_API_KEY = '<your kucoin api key>'
KUCOIN_SECRET = '<your kucoin api key secret>'
KUCOIN_PASSWORD = '<your kucoin password>'

BINANCE_API_KEY = '<your binance api key>'
BINANCE_API_SECRET = '<your binance api key secret>'

MEXC_API_KEY = '<your mexc api key>'
MEXC_API_SECRET = '<your mexc api key secret>'

WALLETS_PATH = 'wallets.json'

account_kucoin = ccxt.kucoin({
    'apiKey': KUCOIN_API_KEY,
    'secret': KUCOIN_SECRET,
    'password': KUCOIN_PASSWORD,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot'
    }
})

account_binance = ccxt.binance({
    'apiKey': BINANCE_API_KEY,
    'secret': BINANCE_API_SECRET,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot'
    }
})

account_mexc = ccxt.mexc({
    'apiKey': MEXC_API_KEY,
    'secret': MEXC_API_SECRET,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot'
    }
})

def withdraw_kucoin(wallet, amount, code, network):
    global account_kucoin
    try:
        account_kucoin.withdraw(
            code = code,
            amount = amount,
            address = wallet,
            tag = None, 
            params = {
                "network": network
            }
        )
        cprint(f">>> Success | {wallet} | {amount}", "green")
    except ExchangeError as error:
        cprint(f">>> Failure | {wallet} | error : {error}", "red")

def withdraw_binance(wallet, amount, code, network):
    global account_binance
    try:
        account_binance.withdraw(
            code = code,
            amount = amount,
            address = wallet,
            tag = None, 
            params = {
                "network": network
            }
        )
        cprint(f">>> Success | {wallet} | {amount}", "green")
    except ExchangeError as error:
        cprint(f">>> Failure | {wallet} | error : {error}", "red")

def withdraw_mexc(wallet, amount, code, network):
    global account_mexc
    try:
        account_mexc.withdraw(
            code = code,
            amount = amount,
            address = wallet,
            tag = None, 
            params = {
                "network": network
            }
        )
        cprint(f">>> Success | {wallet} | {amount}", "green")
    except ExchangeError as error:
        cprint(f">>> Failure | {wallet} | error : {error}", "red")

def __main__():

    with open(WALLETS_PATH, 'r') as j:
        wallets = json.loads(j.read())

    print('Enter currency code:')
    code = input()

    print('Enter amount:')
    amount = input()

    print('Enter network:')
    network = input()

    print('Set timeout (in seconds): ')
    timeout = input()

    print('From what CEX you want to withdraw? (MEXC, Binance, KuCoin)')
    cex_choice = input()

    if(cex_choice.lower() == 'binance'):
        for wallet in wallets:
            withdraw_binance(wallet['address'], amount, code, network)
            time.sleep(int(timeout))
    elif(cex_choice.lower() == 'mexc'):
        for wallet in wallets:
            withdraw_mexc(wallet['address'], amount, code, network)
            time.sleep(int(timeout))
    elif(cex_choice.lower() == 'kucoin'):
        for wallet in wallets:
            withdraw_kucoin(wallet['address'], amount, code, network)
            time.sleep(int(timeout))
    else:
        __main__()

if __name__ == '__main__':
    __main__()