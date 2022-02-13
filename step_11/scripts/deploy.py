from pickle import TRUE
from eth_account import Account
from brownie import FundMe
from scripts.helper import get_accounts

def deploy():
    account = get_accounts()
    fund_me = FundMe.deploy({"from": account}, publish_source=TRUE)
    print(fund_me)
    pass

def main():
    deploy()