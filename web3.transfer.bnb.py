from web3 import Web3
import time, json
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.is_connected())


def get_balance(account_1):
    balance = web3.eth.get_balance(account_1)
    human_readable_balance = web3.from_wei(balance, 'ether')
    print(f"account {account_1} balance: {human_readable_balance}")
    
account_1 = "0x74AA689783ac62A1AFa99a16c206418a493679FF"
get_balance(account_1)
nonce = web3.eth.get_transaction_count(account_1)
print(nonce)

account_2 = '0x13FDE164321fB0125b4CFe8EAB4C228f0207055C'
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.to_wei(0.001, 'ether'),
    'gas': 42000,
    'gasPrice': web3.to_wei('3', 'gwei')
}

# calc private key from script
private_key = 'fill the sender private key here'

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
trans = web3.to_hex(tx_hash)

time.sleep(5)

# transaction info
# transaction = web3.eth.get_transaction(trans)

print(f"transaction ID: {trans}")

get_balance(account_1)