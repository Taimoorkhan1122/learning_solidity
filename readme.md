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

