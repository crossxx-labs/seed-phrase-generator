import sys
import os
from pathlib import Path
import json
import random
import time

seedphrase_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seedphrase')
utils_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils')

sys.path.append(seedphrase_module)
sys.path.append(utils_module)
from transaction import transfer
from utils import process_utils, format


"""
evm transfer coin from one address to another with several middle addresses,
 source address is from seed,
 dest addresses can be derived from seed phrase or original 0x format

Usage: {sys.argv[0]} from_seed_phrase to_seed_or_address middle_loop_address_json_file  start_amount start_index[default 0]
"""

def get_middle_seeds(middle_seeds_file):
    file_path = Path(middle_seeds_file)
    seeds = []
    if not file_path.exists():
        raise Exception(f"{middle_seeds_file} file not exists")
    with open(middle_seeds_file, 'rb') as jf:
        data = json.load(jf)
    for address_item in data['root']['addresses']:
        code, decrypted, stderr = process_utils.aes_decode(address_item['encrypted'])
        if code == 0 :
            seeds += [decrypted]
        else:
            raise Exception(f"decrypt {address_item} error: {stderr}")
    return seeds

def random_loss():
    return random.randint(0,30) * 1e-6

def reduce_amount_on_transfer_error():
    return  random.randint(10,20) * 1e-6

if __name__ == "__main__":
    loss_per_trans = 0.00015
    if len(sys.argv) < 5:
        print(f"Usage: {sys.argv[0]} from_seed_phrase to_seed_or_address middle_loop_address_json_file  start_amount start_index[default 0]")
        sys.exit(1)
    middle_seeds_file = sys.argv[3]
    dest_address = sys.argv[2]
    amount = float(sys.argv[4])
    start_index = 0
    # print(len(sys.argv))
    if (len(sys.argv)) >= 6:
        start_index = int(sys.argv[5])
        print(f"start index from {start_index}")
    source_middle_dest_seeds_or_addresses = [sys.argv[1]] + get_middle_seeds(middle_seeds_file) + [dest_address]
    # source_addrs = mnemonic_to_address(source_seed)
    # print(source_middle_dest_seeds_or_addresses)
    # print(len(source_middle_dest_seeds_or_addresses))
    idx = start_index
    transfer_amount = amount
    while idx < len(source_middle_dest_seeds_or_addresses) -1:
        # transfer from address idx to idx + 1
        src = source_middle_dest_seeds_or_addresses[idx]
        dest = source_middle_dest_seeds_or_addresses[idx + 1]
        loss = loss_per_trans + random_loss()
        transfer_amount -= loss
        # print(f"{idx} source, dest, amount: \n{src}\n {dest}\n {transfer_amount}\n {loss}")
        print(f"processing index {idx}")
        retry = 0
        max_retry = 3
        sleep_seconds = 15
        while retry < max_retry:
            try:
                transfer(src, dest, transfer_amount, sleep_seconds)
                format.print_success(f"index {idx} transfer success with {retry} retry")
                break
            except Exception as e:
                format.print_error(f"get exception: {e}")
                retry += 1
                transfer_amount -= reduce_amount_on_transfer_error()
                print(f"tried {retry} times fail, retry after {sleep_seconds} seconds...")
                time.sleep(sleep_seconds)
        if retry >= max_retry:
            format.print_error(f"transaction error at index {idx}")
            raise Exception(f"transaction error at index {idx}")
                
        idx += 1
        