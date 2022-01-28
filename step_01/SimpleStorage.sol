// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SimpleStorage {
	uint256 number = 1245; // unsigned integer 256 bits
	string name  = "Taimoor khan";
	bool voted  = true;
	address = 0xf72A3765dB24094da92a9D6ee5a7FD614a3ac198;
	
	function getData() public view returns(string){
		return name;		
	}
}
