#!/usr/bin/env python3
from fastecdsa import curve, ecdsa, keys

# You can use any elliptic curve you want
# Generate a new key pair and convert them to hex-strings
priv_key, pub_key = keys.gen_keypair(curve.secp256k1)

priva_key = keys.gen_private_key(curve.secp256k1)

publ_key = keys.get_public_key(priv_key, curve.secp256k1)

print("Your public key (also your wallet address, freely shareable)")
print(pub_key)
print()
print("Your public key (also your wallet address, freely shareable)")
print(publ_key)
print()
print("Your private key (keep this secret! To sign transactions)")
print(priv_key)
print()
print("Your private key (keep this secret! To sign transactions)")
print(priva_key)
