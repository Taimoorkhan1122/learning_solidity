from brownie import FundMe, network, config
from scripts.helper import get_accounts


def deploy():
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_price_feed"]
    account = get_accounts()
    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=True)
    print(fund_me)
    pass

def main():
    deploy()
