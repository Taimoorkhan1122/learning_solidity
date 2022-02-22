from brownie import network, accounts, exceptions, FundMe
from scripts.fund_and_withdraw import fund
from scripts.helper import get_accounts, LOCAL_DEVELOPMENT_ENVIRONMENTS
from scripts.deploy import deploy
import pytest

def test_and_fundme_and_withdraw():
    account =  get_accounts()
    fund_me = deploy()
    entrnace_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrnace_fee})
    tx.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == entrnace_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_only_onwers_can_withdraw():
    if network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENTS:
        pytest.skip("only for local testing")
    
    fund_me = deploy() 
    # blank random accounts
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor, "gas_limit": 100000, "allow_revert": True})

    
