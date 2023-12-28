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

    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI;
    }
    //internal Function to set tokenURI at this tokenID
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        return _tokenURIs[tokenId];
    }
    //check if a tokenID exists in the contract
    function _exists(uint256 tokenId) internal view returns (bool) {
        return _tokenExists[tokenId];
    }
    //transferNFT simply transfers URI at given tokenID in contract from one address to anoither.
    function transferNFT(address from, address to, uint256 tokenId) public {
        
        transferFrom(from, to, tokenId);
    }
    //tradeNFT transfers fromtokenID from 'from' to 'to' and totokenID from 'to' to 'from'
    //We first do some error to check the owners of fromTokenID and toTokenID
    //We also check if the caller is approved to make this transfer.
    function tradeNFT(address from, uint256 fromTokenId, address to, uint256 toTokenId) public {
        require(ownerOf(fromTokenId) == from, "ERC721: caller is not the owner of the from token");
        require(ownerOf(toTokenId) == to, "ERC721: caller is not the owner of the to token");
        require(isApprovedForAll(from, _msgSender()), "ERC721: caller is not approved to transfer the from token");
        require(isApprovedForAll(to, _msgSender()), "ERC721: caller is not approved to transfer the to token");
        safeTransferFrom(from, to, fromTokenId, "");
        safeTransferFrom(to, from, toTokenId, "");
    }


}