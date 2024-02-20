from web3 import Web3
import time

# seedphrase_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seedphrase')

# sys.path.append(seedphrase_module)
from eth_helper import mnemonic_to_address, mnemonic_to_private_key_hex

# bnb
# bsc = "https://bsc-dataseed.binance.org/"

# goerli eth testnet, TODO: refine for general purpose
endpoint = 'https://ethereum-goerli.publicnode.com'
w3 = Web3(Web3.HTTPProvider(endpoint))
# print(web3.is_connected())


def get_balance(account_1):
    balance = w3.eth.get_balance(account_1)
    human_readable_balance = w3.from_wei(balance, 'ether')
    print(f"account {account_1} balance: {human_readable_balance}")
    

"""
evm transfer coin from one address to another, addresses can be derived from seed phrase

Usage: transfer from_seed_phrase  <to_seed_phrase|to_address>  amount sleep_s = 2
"""
def transfer(from_seed, to_seed_or_address, amount, sleep_s = 5):
    account_1 = mnemonic_to_address(from_seed)
    account_2 = to_seed_or_address
    amount = float(amount)
    eth_addr_len = 42
    private_key1 = mnemonic_to_private_key_hex(from_seed)
    if len(account_2) != eth_addr_len:
        account_2 = mnemonic_to_address(account_2)
    get_balance(account_1)
    print(f"{account_1} -> {account_2} {amount}")
    nonce = w3.eth.get_transaction_count(account_1)

    tx = {
        # fix error: ValueError: {'code': -32000, 'message': 'only replay-protected (EIP-155) transactions allowed over RPC'}
        # https://ethereum.stackexchange.com/questions/94412/valueerror-code-32000-message-only-replay-protected-eip-155-transac
        'chainId': 5,
        'nonce': nonce,
        'to': account_2,
        'value': w3.to_wei(amount, 'ether'),
        'gas': 42000,
        'gasPrice': w3.to_wei('3', 'gwei')
    }

    # for goerli eth testnet tx fee is about 0.000063
    signed_tx = w3.eth.account.sign_transaction(tx, private_key1)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    trans = w3.to_hex(tx_hash)

    print(f"sleep for {sleep_s} seconds...")
    time.sleep(sleep_s)

    # transaction info
    # transaction = web3.eth.get_transaction(trans)

    print(f"transaction ID: {trans}")

    # get_balance(account_1)
    # get_balance(account_2)
