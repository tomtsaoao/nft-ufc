from brownie import AdvancedCollectible, accounts, config, interface, network

def get_fighter(fighter_number):
    switch = {0: 'MCGREGOR', 1: 'KHABIB', 2: 'JONES', 3: 'ADESANYA'}
    return switch[fighter_number]

def fund_advanced_collectible(nft_contract):
    dev = accounts.add(config["wallets"]["from_key"]) 
    link_token = interface.LinkTokenInterface(config["networks"][network.show_active()]["link_token"])
    link_token.transfer(nft_contract, 100000000000000000, {"from": dev})