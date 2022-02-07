from eth_utils import address
from brownie import accounts, SimpleStorage


def test_deploy():
    # arrange
    account = accounts[0]
    # act
    simple_storgae = SimpleStorage.deploy({"from": account})
    expected = 0
    # assert
    assert expected == simple_storgae.retrieve()


def test_updating():
    # arrange
    account = accounts[0]
    simple_storgae = SimpleStorage.deploy({"from": account})

    # act
    txn = simple_storgae.store(5, {"from": account})
    expected = 5
    txn.wait(1) 
    # assert
    assert expected == simple_storgae.retrieve()