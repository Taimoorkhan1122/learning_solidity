from brownie import MockV3Aggregator,network, accounts,config 
from web3 import Web3

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = 20000
LOCAL_DEVELOPMENT_ENVIRONMENTS = ["development", "ganache-local-chain"]

def get_accounts():
    if network.show_active() in LOCAL_DEVELOPMENT_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mock():
    print(f"The active network is {network.show_active()}")
    account = get_accounts()
    if len(MockV3Aggregator) <= 0:
        print("Deploying Mocks...")
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(INITIAL_VALUE, "ether"), {"from": account}
        )
        print("Mocks Deployed!")