import blockcypher
import blockcypher.utils as bcUtils
from datetime import datetime
from models import Oap

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
    is_valid = blockcypher.is_valid_address(address)
    is_coin_valid = bcUtils.is_valid_coin_symbol(symbol)
    is_valid_for_coin = bcUtils.is_valid_address_for_coinsymbol(address, symbol)
    print("is {} a valid address? : {}".format(address, is_valid))
    print("is {} a valid coin on source 'blockcypher'? : {}".format(symbol, is_coin_valid))
    print("is {} a valid address for coin {}? : {}".format(address, symbol, is_valid_for_coin))
    
    if is_valid and is_coin_valid and is_valid_for_coin:
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
search_address_details('C9PCEfkWhK5ohGxNU957SxKg9qdcg3XRSw')
# search_address('C9PCEfkWhK5ohGxNU957SxKg9qdcg3XRSw')