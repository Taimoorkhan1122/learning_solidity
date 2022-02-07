from brownie import accounts, config, SimpleStorage


def deploy_contract():
    # account =  accounts[0]

    # account =  accounts.load("my_local_account")
    account = accounts.add(config["wallets"]["from_key"])
    # this single line is equal to all the stuff we did in step 09 to deploy our contract

    simple_storage = SimpleStorage.deploy({"from": account})
    print("------- DEPLOYING CONTRACT ------- \n",simple_storage)
    stored_value = simple_storage.retrieve()
    print("stored Value : ", stored_value)

    transaction = simple_storage.store(23, {"from": account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve()
    print("Updated Value : ", updated_value)
    pass


def main():
    deploy_contract()
