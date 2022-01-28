// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// storageFactory pattern: A pattern where one contract can anohther pattern

import "./SimpleStorage.sol";

contract StorageFactory {
    SimpleStorage[] public simpleStorageArr;

    function createSimpleStorage() public {
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArr.push(simpleStorage);
    }

    function sfStore(uint256 _index, uint256 _number, string memory _name) public {
        // first we need address of the contract stored in array
        // then we need to provide the abi of that contract to the SimpleStorage object call
        //this line has an explicit cast to the address type and initializes a new SimpleStorage object from the address 
        SimpleStorage(address (simpleStorageArr[_index])).store(_number, _name, true);
    }

    function sfGet(uint256 _index, string memory _name) public view returns(uint256) {
        return SimpleStorage(address (simpleStorageArr[_index])).retrieve(_name);
    }

}