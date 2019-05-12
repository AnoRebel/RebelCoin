#!/usr/bin/env python3
from blockchain import Blockchain, Transaction
from fastecdsa import curve, ecdsa, keys

# Your private key goes here
priv_key = keys.gen_private_key(curve.secp256k1)

# From that we can calculate your public key(which doubles as your wallet address)
pub_key = keys.get_public_key(priv_key, curve.secp256k1)
myWalletAddress = hex(int(str(pub_key.x)+str(pub_key.y)))

# Create new instance of Blockchain class
print('Initialize coin')
rebelCoin = Blockchain()

# Create a transaction & sign it with your key
print('1st trans')
tx1 = Transaction(myWalletAddress, '123456789', 100)
tx1.signTransaction(priv_key)
# These try/except blocks are neccessary for now due to a bug i have where
# there's either an ecdsa error or a key error, but reruning fixes it
try:
    try:
        rebelCoin.addTransaction(tx1)
    except ecdsa.EcdsaError:
        rebelCoin.addTransaction(tx1)
except:
    rebelCoin.addTransaction(tx1)
print()

# Mine block
rebelCoin.minePendingTransactions(myWalletAddress)

# Create second transaction
print('2nd trans')
tx2 = Transaction(myWalletAddress, '987654321', 50)
tx2.signTransaction(priv_key)
rebelCoin.addTransaction(tx2)
# These try/except blocks are neccessary for now due to a bug i have where
# there's either an ecdsa error or a key error, but reruning fixes it
try:
    try:
        rebelCoin.addTransaction(tx2)
    except ecdsa.EcdsaError:
        rebelCoin.addTransaction(tx2)
except:
    rebelCoin.addTransaction(tx2)
print()

# Mine block
rebelCoin.minePendingTransactions(myWalletAddress)

print()
print('Balance of xavier is ')
print(rebelCoin.getBalanceOfAddress(myWalletAddress))

# Uncomment this line if you want to test tampering with the chain
# rebelCoin.chain[1].transactions[0].amount = 10

# Check if the chain is valid
print()
print('Blockchain valid?', 'Yes' if rebelCoin.isChainValid() == True else 'No')
