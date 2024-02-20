import sys
import os

seedphrase_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seedphrase')
utils_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils')

sys.path.append(seedphrase_module)
sys.path.append(utils_module)
from transaction import transfer


"""
evm transfer coin from one address to another, addresses can be derived from seed phrase

Usage: {sys.argv[0]} from_seed_phrase  <to_seed_phrase|to_address>  amount
"""

    
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} from_seed_phrase  <to_seed_phrase|to_address> amount")
        sys.exit(1)
    transfer(sys.argv[1], sys.argv[2], sys.argv[3])