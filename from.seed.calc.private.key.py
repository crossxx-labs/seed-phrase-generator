
import sys
import os

"""
calc private key from seed phrase for eth / bnb

Usage: {sys.argv[0]} seed_phrase

"""
seedphrase_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seedphrase')

sys.path.append(seedphrase_module)

from eth_helper import mnemonic_to_private_key, ETH_DERIVATION_PATH

if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        print(f"Usage: {sys.argv[0]} seed_phrase")
        sys.exit(1)
    mnemonic = sys.argv[1]
    print(mnemonic_to_private_key(mnemonic,
            str_derivation_path=f'{ETH_DERIVATION_PATH}/0').hex())