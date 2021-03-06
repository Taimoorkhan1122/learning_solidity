# Learnign Blockchain and Web 3.0

## This repository is a part of learning Solidity, and Blockchain.

I will keep updating this repo as I learn new topics or found any useful links that helped me learning.

Useful links: <br/>
[how blockchain works under the hood](https://www.youtube.com/watch?v=Lx9zgZCMqXE&list=PLC36LpxxRvvmcsY5OF2cPlhLKoHjZS4Dm&index=1)

[What is Proof of Work: explained](https://www.youtube.com/watch?v=M576WGiDBdQ&list=PLC36LpxxRvvmcsY5OF2cPlhLKoHjZS4Dm&index=2)

[What is Proof of Stack](https://www.youtube.com/watch?v=psKDXvXdr7k)

[Byzantine Generals Problem (Consensus mechanism in BTC)](https://www.youtube.com/watch?v=dfsRQyYXOsQ&t=182s)


[Solidity, Blockchian and Smart contract course](https://www.youtube.com/watch?v=M576WGiDBdQ&list=PLC36LpxxRvvmcsY5OF2cPlhLKoHjZS4Dm&index=2)


# Working with Brownie

### Initialize a new project
To initialize a new project use 
```
brownie init
``` 

### Run Scripts
```
brownie run <name of script file>
```

### Import random accounts
```
from brownie import accounts

def deploy_contract():
    account =  accounts[0]
```
This will spin a local ganache cli and get 10 random accounts


### Import local accounts
Run this command to add new account by entering private key

```
$ brownie accounts new <name_of_new_account>
```
it will ask to enter new private key, go to your wallet and past the private key

```
from brownie import accounts

def deploy_contract():
    account =  accounts.load("name_of_new_account")
```
This import your own account

### Access contract in Brownie

We can directly access our Contract inside our deploy.py script file. Brownie will take care of reading and compiling the contract.

using `.deploy({"from": <sender account>)` will create a trasaction from provided account and deploy it to ganache local chain


### Writing test for Contracts
Writing test is crutial for developing smart contracts, it saves lots of efforts to debug if the contracts are working as expected or not. We are using pytest for testing our smart contracts. Brownie provides same utilities as pytest using it under the hood.

We follow these steps when writing a test
- Arrange: arrange all pieces of test
- Act: create contract calls or other runtime work
- Assert: assert the result of actions to the expected output

### Brownie Console

For testing our contracts, we can use Brownie shell to access our contract without manually deploying it


### Verify deployed Contracts
To verify deployed contracts progammatically you need to get access to api key from etherscan. Create an account and add you project to get one.

Add the api key to .env as `ETHERSCAN_TOKEN`Then inside `deploy()` function add `publish_source=TRUE`