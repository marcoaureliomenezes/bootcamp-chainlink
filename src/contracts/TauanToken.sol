//SPDX-License-Identifier: MIT

pragma solidity 0.5.2;

import '@openzeppelin/contracts/token/ERC20/ERC20Mintable.sol';

contract TauanToken is ERC20Mintable{
        string public name = "Tauan Menezes Token";
        string public symbol = "TMT";
        uint8 public decimals = 2;
}