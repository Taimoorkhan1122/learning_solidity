from brownie import FundMe
from scripts.helper import get_accounts

def fund():
    fund_me = FundMe[-1]
    account = get_accounts()
    enterance_fee = fund_me.getEntranceFee()
    print(f"Entrance fee is {enterance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": enterance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_accounts()
    print("withdrawing funds")
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()
