// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
library priceConverter{

    function ethPrice() internal view returns(uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e);
       
        (,int256 eth_usd_price,,,)=priceFeed.latestRoundData();
        uint256 eth_usd= uint256(eth_usd_price);
        return eth_usd*10000000000;
    }

    function price_in_usd(uint256 amount) internal view returns(uint256){
        uint256 conversion_rate=ethPrice();
        return amount*conversion_rate/1000000000000000000;
    }
}