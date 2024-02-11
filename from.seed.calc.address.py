
import sys
import os

""""
calc eth/bsc address from seed phrase
"""
seedphrase_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seedphrase')

sys.path.append(seedphrase_module)

from eth_helper import mnemonic_to_address, ETH_DERIVATION_PATH

if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        print(f"Usage: {sys.argv[0]} seed_phrase")
        sys.exit(1)
    mnemonic = sys.argv[1]
    print(mnemonic_to_address(mnemonic))