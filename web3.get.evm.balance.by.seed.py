from web3 import Web3
import time, json
import sys
import os

seedphrase_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seedphrase')
utils_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils')

sys.path.append(seedphrase_module)
sys.path.append(utils_module)
from eth_helper import mnemonic_to_address
from transaction import get_balance


"""
get balance of an address(or implied from seed phrase)

Usage: {sys.argv[0]} seed_phrase | evm_address
"""

    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} seed_phrase | evm_address")
    account_1 = sys.argv[1]
    eth_addr_len = 42
    if len(account_1) != eth_addr_len:
        # seed phrase to address
        account_1 = mnemonic_to_address(account_1)
    get_balance(account_1)