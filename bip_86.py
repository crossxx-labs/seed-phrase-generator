"""Example of keys derivation using BIP44 BIP49 BIP84 BIP86 on main net and test net."""

from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip44Changes, Bip86, Bip86Coins

import sys

"""
print bitcoin bip86 addresses from seed phrase

Usage: {sys.argv[0]} [seed_phrase]
if no seed_phrase specified, auto generate it.
referenced from bip_utils official examples
"""

if __name__ == "__main__":
    # Generate random mnemonic
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
    if len(sys.argv) > 1:
        mnemonic = sys.argv[1]
    # Generate seed from mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

    # Construct from seed
    # bip86_mst_ctx = Bip86.FromSeed(seed_bytes, Bip86Coins.BITCOIN_TESTNET)
    bip86_mst_ctx = Bip86.FromSeed(seed_bytes, Bip86Coins.BITCOIN)

    # Derive BIP86 account keys: m/86'/0'/0'
    bip86_acc_ctx = bip86_mst_ctx.Purpose().Coin().Account(0)
    # Derive BIP86 chain keys: m/86'/0'/0'/0
    bip86_chg_ctx = bip86_acc_ctx.Change(Bip44Changes.CHAIN_EXT)
    
    bip86_addr_ctx = bip86_chg_ctx.AddressIndex(0)
    # print(f"  {i}. Address public key (extended): {bip86_addr_ctx.PublicKey().ToExtended()}")
    # print(f"  {i}. Address private key (extended): {bip86_addr_ctx.PrivateKey().ToExtended()}")
    print(f"{mnemonic}")
    print(f"{bip86_addr_ctx.PublicKey().ToAddress()}")
