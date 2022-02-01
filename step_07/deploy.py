import json
from solcx import compile_standard, install_solc

# first we need to open our contract file
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    
# next we will compile the source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol", {"content": simple_storage_file}},
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
