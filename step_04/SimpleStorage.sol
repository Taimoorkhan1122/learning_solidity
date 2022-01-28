// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 favouriteNumber;

    //structs: similar to structs in other languages
    struct Person {
        uint favouriteNumber;
        string name;
        bool voted;
    }

    // mappings: maps a key to its corresponding value
    mapping(string => uint) public nameToNumber;
    
    // defining an array
    Person[] public collection;
    // this functins is public and can be accessed by everyone
    function store(uint256 _favNum) public {
        favouriteNumber += _favNum;
    }

    // this function is readonly and returns value
    function retrieve(string memory _name) public view returns(uint256){
        return nameToNumber[_name];
    }

    function store(uint _favouriteNumber ,string memory _name, bool _voted) public {
        collection.push(Person(_favouriteNumber, _name, _voted));
        nameToNumber[_name] = _favouriteNumber;
    }
}
