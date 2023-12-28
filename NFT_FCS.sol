// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
// Import necessary libraries

//Specify token inherits from ERC721
contract MyNFT is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    //Store tokenURIs for each tokenIDs,_tokenExists is boolean array to return if a particular token exists or not
    mapping(uint256 => string) private _tokenURIs;
    mapping(uint256 => bool) private _tokenExists;

    constructor() ERC721("MyNFT", "NFT") {}
    //Function to mint NFT
    //recipient address is the wallet address,tokenID is the ID of the token,tokenURI is IPFS URI
    function mintNFT(address recipient, uint256 tokenId, string memory tokenURI) public {
        _safeMint(recipient, tokenId);
        _setTokenURI(tokenId, tokenURI);
    }
    //internal Function to set tokenURI at this tokenID
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        return _tokenURIs[tokenId];
    }
    //check if a tokenID exists in the contract
    function _exists(uint256 tokenId) internal view returns (bool) {
        return _tokenExists[tokenId];
    }
}
