// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;
// Aggregator Interface 
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    // mapping sender address to amount funded
    mapping(address => uint256)  public addressToAmountFunded;
    address[] public funders;
    address private owner;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) {
        owner = msg.sender;
        // providing the address of ETH to USD contract
        // the contract has implemented AggregatorV3Interface methods 
        priceFeed = AggregatorV3Interface(_priceFeed);

    }

    function getOwner() public view returns(address) {
        return owner;
    }

    // fund function to submit amount to address
    function fund() public payable {
        // 18 digit number to be compared with donated amount
        uint256 minimumUSD  = 50 * 10 ** 18;
        require(getConversionRates(msg.value) >= minimumUSD, "You need more ETH!");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
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


    function getEntranceFee() public view returns (uint256){
        // minimun USD
        uint256 minimumUSD = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        return (minimumUSD * precision)/ price;
    }
    
    // modifiers, theses are similar to decorators in OOP. 
    // Use this when you want to do some testing befor executing the funtion.
    modifier adminOnly {
        require(msg.sender == owner, "Only owner of the contract can withdraw");
        _;
    }

    function withdraw() public adminOnly payable  {
        payable(msg.sender).transfer(address(this).balance);

        for(uint256 senderIndex=0; senderIndex < funders.length; senderIndex++){
            address funder = funders[senderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}