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
savjeeCoin = Blockchain()

# Create a transaction & sign it with your key
print('1st trans')
tx1 = Transaction(myWalletAddress, '123456789', 100)
tx1.signTransaction(priv_key)
try:
    try:
        savjeeCoin.addTransaction(tx1)
    except ecdsa.EcdsaError:
        savjeeCoin.addTransaction(tx1)
except:
    savjeeCoin.addTransaction(tx1)
print()

# Mine block
savjeeCoin.minePendingTransactions(myWalletAddress)

# Create second transaction
print('2nd trans')
tx2 = Transaction(myWalletAddress, '987654321', 50)
tx2.signTransaction(priv_key)
savjeeCoin.addTransaction(tx2)
try:
    try:
        savjeeCoin.addTransaction(tx2)
    except ecdsa.EcdsaError:
        savjeeCoin.addTransaction(tx2)
except:
    savjeeCoin.addTransaction(tx2)
print()

# Mine block
savjeeCoin.minePendingTransactions(myWalletAddress)

print()
print('Balance of xavier is ')
print(savjeeCoin.getBalanceOfAddress(myWalletAddress))

# Uncomment this line if you want to test tampering with the chain
# savjeeCoin.chain[1].transactions[0].amount = 10

# Check if the chain is valid
print()
print('Blockchain valid?', 'Yes' if savjeeCoin.isChainValid() == True else 'No')
