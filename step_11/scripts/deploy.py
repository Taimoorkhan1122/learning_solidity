from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helper import get_accounts, deploy_mock, LOCAL_DEVELOPMENT_ENVIRONMENTS


def deploy():
    if network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_price_feed"]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    account = get_accounts()
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(fund_me)
    return fund_me

def main():
    deploy()
