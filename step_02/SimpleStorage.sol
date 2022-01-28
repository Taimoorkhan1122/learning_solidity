// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 favouriteNumber;

    // this functins is public and can be accessed by everyone
    function store(uint256 _favNum) public {
        favouriteNumber += _favNum;
    }

    // this function is readonly and returns value
    function retrieve(string memory _name) public view returns(uint256){
        return favouriteNumber;
    }

    // this function does not mutate state and cannot access state
    function increment(string memory word) public pure returns(string memory) {
        return word;
    } 

}
