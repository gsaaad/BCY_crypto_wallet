import blockcypher
from blockcypher.utils import is_valid_address_for_coinsymbol

# using bcy test accounts / fund
symbol = 'bcy'

#user1 mongoDB original address in OAP
user1_OG_address = 'C9PCEfkWhK5ohGxNU957SxKg9qdcg3XRSw'
user1_priv_address = 'f3f773d1b97f4e094fa653d27aa4a6eda73ddbf6177519213c0099e3b5a308b1'
user1_pub_address = '0227756ea395baf371bf01acc603bdb470fa288ca138aa80d4c87ff6452ec49d36'
user1_wif = 'BwWGcVNErxct8qVFHxTnE9VzNQTRfhXhqHMFo5qa7cmf7rQkLRwN'
user1_OAP_address ='1C9PCEfkWhK5ohGxNU957SxKg9qdcgFQaTP'


user2_OG_address = 'C9YZZVTAz7avsdA4azzsrm1sa3X4uGJBvX'
user2_priv_address = '7aea9c58dd4e5c24421239a48ac30dca5e71675e606e209726d1cdee107afea9'
user2_pub_address = '0384a0db4b7e1d021b98c68a367cd7d5e0bb6cf4454f921ccbde0c78590dc396dd'
user2_wif = 'BsSxt7wGCkc6xrtDNYP3qocbfp1BwkU2d6HBvQgxchyggdyAuTNe'
user2_oap_address = '1C9YZZVTAz7avsdA4azzsrm1sa3X4wUsb5B'

#token
token='df29ec63ab9047cc9520edae52e1ead2'


#get address overview
# address_overview = blockcypher.get_address_overview(user1_OG_address, coin_symbol=symbol)
# print("Address Overview of user 1 OG address",address_overview)

#get address details
# address_details = blockcypher.get_address_details(user1_OG_address, coin_symbol=symbol, show_confidence=True, include_script=True)
# print("Address_Details",address_details)

# address_total_balance = blockcypher.get_total_balance(user1_OG_address, coin_symbol=symbol)
# print("total Balance for {} is: ".format(user1_OG_address), address_total_balance)

# transfers satoshis to number of real BTC. v this example is bcy amount from address
# total_base_balance = blockcypher.from_base_unit(address_total_balance, 'btc')
# print("Base balance: ",total_base_balance)

# total_num_transactions = blockcypher.get_total_num_transactions(user1_OG_address, coin_symbol=symbol)
# print("Total transactions of user 1 og address: ",total_num_transactions)

# current_block_height = blockcypher.get_latest_block_height(coin_symbol=symbol)
# print("Current Block Height with symbol {}".format(symbol), current_block_height)

# current_block_height = blockcypher.get_latest_block_height()
# print("Current Block Height with symbol {}".format('btc'), current_block_height)

# print("Coins from blockcypher coin constant list", blockcypher.constants.COIN_SYMBOL_LIST)

# valid_address = blockcypher.is_valid_address(user1_OG_address)
# print("is user 1 OG address: {} a valid address? [True = yes, False = no]:  ".format(user1_OG_address), valid_address)

# list_of_wallet_names = blockcypher.list_wallet_names(token)
# print("list of wallet names", list_of_wallet_names)


#simple spend
print("balance of user 1 OG ADDRESS {}".format(blockcypher.get_total_balance(user1_OG_address, coin_symbol=symbol)))
print("balance of user 2 OG ADDRESS {}".format(blockcypher.get_total_balance(user2_OG_address, coin_symbol=symbol)))

print("is USER 1 OG address valid address {} and valid for coin BCY {}".format(blockcypher.is_valid_address(user1_OG_address), is_valid_address_for_coinsymbol(user1_OG_address, coin_symbol=symbol)))
print("is USER 1 PRIV address valid address {} and valid for coin BCY {}".format(blockcypher.is_valid_address(user1_priv_address), is_valid_address_for_coinsymbol(user1_priv_address, coin_symbol=symbol)))

print("is USER 2 OG address valid address {} and valid for coin BCY {}".format(blockcypher.is_valid_address(user2_OG_address), is_valid_address_for_coinsymbol(user2_OG_address, coin_symbol=symbol)))



is_user1_OG_address_valid_for_coin = is_valid_address_for_coinsymbol(user1_OG_address, coin_symbol=symbol)
# print("user1 OG is valid for coin BCY ??", is_user1_priv_valid_for_coin)

is_user2_OAP_address_valid_for_coin = is_valid_address_for_coinsymbol(user2_oap_address, coin_symbol=symbol)
# print("is user2 OAP address a valid address for bcy", is_oap_address_valid_for_coin)


#todo sending 2222 from user 1 OG, to user 2 OG
satoshi_amount = 7777
inputs = [{'address': user1_OG_address}]
outputs = [{'address': user2_OG_address, "value": satoshi_amount}]

print("sending payment from user 1 OG address to user 2 OG address with {}".format(satoshi_amount))
# print("user1 OG is valid for coin BCY ??", is_user1_priv_valid_for_coin)
# print("is user2 OAP address a valid address for bcy", is_oap_address_valid_for_coin)

create_unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol=symbol, api_key=token, verify_tosigntx=True,change_address=user1_OG_address)

print("unsigned tx", create_unsigned_tx)
to_sign_tx = {}
to_sign_tx['tosign_tx'] = create_unsigned_tx['tosign_tx']
to_sign_tx['tosign'] = create_unsigned_tx['tosign']
print("to_sign_tx: ", to_sign_tx)
to_sign = '799d0a0a878b3b51fef88c902d617c3bcc995f6aba7e2cbc7a8925a09563c4e7'
print("toSign = ", to_sign)

verify_unsigned = blockcypher.verify_unsigned_tx(unsigned_tx=to_sign_tx, outputs=outputs, coin_symbol=symbol, change_address=user1_OG_address)
print(verify_unsigned)


input_addresses = blockcypher.get_input_addresses(create_unsigned_tx)
print("INPUT ADDRESES", input_addresses)

tx = to_sign_tx['tosign']
print(tx)

# user 1 priv and public
tx_signatures = blockcypher.make_tx_signatures(tx,privkey_list=[user1_priv_address], pubkey_list=[user1_pub_address])
print("trasnaction signatture is: ", tx_signatures)

print("broadcasting!")
addresses_pubkeys = [user1_pub_address]
broadcast_tx = blockcypher.broadcast_signed_transaction(create_unsigned_tx, tx_signatures, pubkeys=addresses_pubkeys, coin_symbol=symbol, api_key=token)

print("broadcast is:.... ", broadcast_tx)
