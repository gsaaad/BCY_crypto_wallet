import blockcypher
def search_address(address):
    
    # todo 1st check databa
    print("searching for address in database..")
    
    #todo if no record in data base, query API to retrieve latest data
    print("Consuming API: Searching for address..")

def search_address_details(address, symbol='bcy'):
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
search_address_details('C9PCEfkWhK5ohGxNU957SxKg9qdcg3XRSw','bcy')