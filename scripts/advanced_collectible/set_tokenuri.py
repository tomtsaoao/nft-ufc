from brownie import AdvancedCollectible, network, config, accounts
from ...scripts.helpful_scripts import get_fighter

fighters_metadata_dic = {
    "MCREGOR": "https://ipfs.io/ipfs/QmNshpfGgnUr5WnVNsv4NXyHVeijVnc2fLdXhBJy6fpV7m?filename=0-MCGREGOR.json",
    "KHABIB": "https://ipfs.io/ipfs/QmRrbfEfZC8VxfTKrBRsnjTrzNKA33DwQhivRXsFd3GoSY?filename=1-KHABIB.json",
    "JONES": "https://ipfs.io/ipfs/Qmcy5HbzsFJrJQS5n11LeMjAvAQEs55x9YoxfwgWz8rJZX?filename=2-JONES.json",
    "ADESANYA" : "https://ipfs.io/ipfs/QmdyPPrAxF5dE559i8c8kGgsWtWDKWGe464PXDagcoQqkC?filename=3-ADESANYA.json"
}

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print("The number of tokens you've deployed is: " + str(number_of_advanced_collectibles))
    for token_id in range(number_of_advanced_collectibles):
        fighter = get_fighter(advanced_collectible.tokenIdToFighter(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, advanced_collectible, fighters_metadata_dic[fighter])
        else:
            print("Skipping {}, we've already set that tokenURI!".format(token_id))

def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print("Awesome! You can now view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print("Please give up to 20 mins and hit refresh metadata button")
