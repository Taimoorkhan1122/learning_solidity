from brownie import accounts, config

def deploy_contract():
    # account =  accounts[0]
    
    # account =  accounts.load("my_local_account")
    account =  accounts.add(config["wallets"]["from_key"])
    print(account)
    pass

def main():
    deploy_contract()
