from brownie import AdvancedCollectible, accounts, config
from ...scripts.helpful_scripts import get_fighter
import time

STATIC_SEED = 1234

def main():
    dev = accounts.add(config['wallets']['from_key'])
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    transaction = advanced_collectible.createCollectible(STATIC_SEED, "None", {"from": dev})
    transaction.wait(1)
    requestId = transaction.events['requestedCollectible']['requestId']
    token_id = advanced_collectible.requestIdToTokenId(requestId)
    time.sleep(45)
    fighter = get_fighter(advanced_collectible.tokenIdToFighter(token_id))
    print('Fighter of tokenId {} is {}'.format(token_id, fighter))