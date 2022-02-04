import json
from solcx import compile_standard, install_solc
from web3 import Web3
from dotenv import load_dotenv
import os


load_dotenv()

# first we need to open our contract file
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()


# installing solidity compiler
print("Installing...")
install_solc("0.8.0")

# next we will compile the source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

# writing compiled json file
with open("compiledCode.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]

# connection to Ganache RPC server
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))

chian_id = 1337
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = os.getenv("PRIVATE_KEY")
# create contract in python: this will create an instance of Contract object in python
# Build the contract & deploy Transaction
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# when we make transaction to blockchain we are making a
# state change in our contract on blockchain

nonce = w3.eth.getTransactionCount(my_address)  # NONCE: Number once used
# 1. Create Transaction
# 2. Sign Transaction
# 3. Send Transaction

initial_transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chian_id,
        "from": my_address,
        "nonce": nonce,
    }
)


def createTransaction(transaction):
    print("signing transcation.... ")
    # signing transaction (message) with private key
    signed_tx = w3.eth.account.sign_transaction(
        transaction, private_key=private_key
    )

    # sending transaction
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    print("waiting for receipt.... ")
    tx_reciept = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_reciept


# interacting with Contract

# For interacting with deployed contract we need:
# Contract ABI
# Contract address

contract_reciept = createTransaction(initial_transaction)

# First we will create an instance of our contract class
simple_storage = w3.eth.contract(
    address=contract_reciept.contractAddress, abi=abi
)

# There are two ways of interacting with contract
# call -> simulating function call with no state change and returning a value
# transact -> simulating a function call with state change
print("initial value: ")
print(simple_storage.functions.retrieve().call())

print("making store call.... ")

simple_storage_transaction = simple_storage.functions.store(25).buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chian_id,
        "from": my_address,
        "nonce": nonce+1,
    }
)


simple_transation_reciept = createTransaction(simple_storage_transaction)


print(f"Transaction Reciept:{simple_transation_reciept} \nUpdated value: {simple_storage.functions.retrieve().call()}")
