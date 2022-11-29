import blockcypher
import blockcypher.utils as bcUtils
from datetime import datetime
import requests
from .models import Oap

def search_address(address):
    date_search = datetime.now()
    print(date_search)
    # todo 1st check databa
    print("searching for address in database..")
    try:
        result = Oap.find_one({'original_address':address})
        if result is not None:
            print("Address was found in database",result)
            return result
        #todo if no record in data base, query API to retrieve latest data
        else:
            print("Consuming API: Searching for address..")
            details_address =search_address_details(address)
            print("searched details for {} are {}".format(address, details_address))
            
    except:
        print("could not find address")
    finally:
        print("searching for address in database complete..")
def search_address_details(address, symbol='bcy'):

    is_valid = is_valid_pre_payment(address,symbol)
    if is_valid:
        address_details = blockcypher.get_address_details(address, symbol)
        balance = address_details['balance']
        unconfirmed_balance = address_details['unconfirmed_balance']
        total_balance = address_details['final_balance']
        numTx = address_details['n_tx']
        unconfirmed_numTx = address_details['unconfirmed_n_tx']
        total_numTx = address_details['final_n_tx']
        total_sent = address_details['total_sent']
        total_received = address_details['total_received']
        # print(balance, unconfirmed_balance, total_balance,numTx,unconfirmed_numTx,total_numTx, total_sent, total_received)
        address_details = {"balance": balance, "unconfirmed_balance": unconfirmed_balance, "total_balance": total_balance, "numTx": numTx, "unconfirmed_numTx": unconfirmed_numTx, "total_numTx": total_numTx, "total_sent": total_sent, "total_received": total_received}
        return address_details
def is_valid_pre_payment(address,symbol='bcy'):
    is_valid = blockcypher.is_valid_address(address)
    is_coin_valid = bcUtils.is_valid_coin_symbol(symbol)
    is_valid_for_coin = bcUtils.is_valid_address_for_coinsymbol(address, symbol)
    print("is {} a valid address? : {}".format(address, is_valid))
    print("is {} a valid coin on source 'blockcypher'? : {}".format(symbol, is_coin_valid))
    print("is {} a valid address for coin {}? : {}".format(address, symbol, is_valid_for_coin))
    valid = is_valid and is_coin_valid and is_valid_for_coin
    return valid
def get_top_fifteen_coins():
    url = "https://investing-cryptocurrency-markets.p.rapidapi.com/coins/list"
    querystring = {"edition_currency_id":"12","time_utc_offset":"28800","lang_ID":"1","sort":"MARKETCAP_DN","page":"1"}
    headers = {
        "X-RapidAPI-Key": "204482477cmshdd6f520fedecd46p1ea1fbjsne7e8a3e634f6",
        "X-RapidAPI-Host": "investing-cryptocurrency-markets.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    total_data = response.json()['data']

    data_dict = total_data[0]
    ("---------------")
    screen_data = data_dict['screen_data']
    crypto_data = screen_data['crypto_data']
    # get top 15
    top_fifteen = crypto_data[:15]
    return top_fifteen
def get_crypto_news():
    url = 'https://newsdata.io/api/1/news?apikey=pub_138138276edf3ab14b519df5a6f4315255963&q=crypto&country=ca&language=en'
    response = requests.request("GET", url)
    total_data = response.json()['results']
    top_fifteen_news = total_data[:10]
    
    return top_fifteen_news
# def create_funded_btc_address():
#     print("creating new BTC priv/pub/address  ")
#     url ='https://api.blockcypher.com/v1/bcy/test/addrs?token=df29ec63ab9047cc9520edae52e1ead2'
#     response = requests.request("POST",url)
#     new_wallet = response.json()['results']
#     print(new_wallet)
#     return new_wallet
