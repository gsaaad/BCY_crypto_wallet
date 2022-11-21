import blockcypher

def check_valid_address(address):
    print('checking validity of address: {}'.format(address))
    print('address is ',address)
    print('length of address:', len(address))
    print('----------------------')
    is_valid = blockcypher.is_valid_address(address)
    print('is address {} valid : {}'.format(address, is_valid))
    return is_valid
    
    
