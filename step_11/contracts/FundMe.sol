// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;
// Aggregator Interface 
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    address public owner;
    AggregatorV3Interface public priceFeed;
    constructor(address _priceFeed){
        owner = msg.sender;
        // providing the address of ETH to USD contract
        // the contract has implemented AggregatorV3Interface methods 
        priceFeed = AggregatorV3Interface(_priceFeed);

    }

    // mapping sender address to the amount funded
    mapping(address => uint256)  addressToAmountFunded;

    // fund function to submit amount to address
    function fund() public payable {
        // 18 digit number to be compared with donated amount
        uint256 minimumUSD  = 50 * 10 ** 18;
        require(getConversionRates(msg.value) >= minimumUSD, "You need more ETH!");
        addressToAmountFunded[msg.sender] += msg.value;
    }

    function getVersion() public view returns(uint256){
        return priceFeed.version();
    }

    function getPrice() public view returns(uint256){
        (,int256 answer,,,) = priceFeed.latestRoundData();
        // ETH/USD rate in 18 digit 
        return uint256(answer * 10000000000);
    }

    function getConversionRates(uint256 ethAmount) public view returns(uint256){
        uint256 ethPrice = getPrice();
        uint256 ethInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethInUsd;
    }

}