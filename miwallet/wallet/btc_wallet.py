import requests
from blockcypher import send_faucet_coins
def create_btc_address():
    print("creating new BTC priv/pub/address")
    url ='https://api.blockcypher.com/v1/btc/test3/addrs?token=df29ec63ab9047cc9520edae52e1ead2'
    try:
        response = requests.post(url)
        if(response.status_code == 201):
            new_wallet = response.json()
            print(new_wallet)
            return new_wallet
    except:
        print("Error in creating new BTC Wallet... Try again later..")
# create_btc_address()

{
    'private': 'ef4a0773386fc9d2056231ec3f00627a6637eb6a96215071763077a032792e00',
    'public': '0221d9fa6d54f7e6ee6b84cab4dc1c489337477cc4d60686e9f5b3efd0ebbb6421', 
    'address': 'Bv1UrkY798Ldi14rvNwuCqR1FVNe1jRzc8', 
    'wif': 'BwMBFvDeDq54UP3gaq9A5iWWxAisGS9Zp7EeBjgU78f5SViLsbaQ'}
def fund_btc_address(address, amount, symbol='btc-testnet'):
    token = 'df29ec63ab9047cc9520edae52e1ead2'
    
    print("funding address {} with currency {} and amount {}".format(address, symbol, amount))
    send_faucet_coins(address_to_fund=address, satoshis=amount,api_key=token, coin_symbol=symbol)
fund_btc_address('n1co7hwPArc7w2Q2dVv87w76ThsRbfWBYc', 100)