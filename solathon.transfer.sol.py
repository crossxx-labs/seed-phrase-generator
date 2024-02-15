from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair
import sys

"""
Usage: {sys.argv[0]} sender_private_key receiver_address
"""

if __name__ == "__main__":
    if (len(sys.argv) <= 2):
        print(f"Usage: {sys.argv[0]} sender_private_key receiver_address")
        sys.exit(1)
    client = Client("https://api.mainnet-beta.solana.com")

    sender = Keypair.from_private_key(f"{sys.argv[1]}")
    receiver = PublicKey(f"{sys.argv[2]}")
    amount = 0.001 * 1e9

    instruction = transfer(
            from_public_key=sender.public_key,
            to_public_key=receiver, 
            lamports=int(amount)
        )

    transaction = Transaction(instructions=[instruction], signers=[sender])

    result = client.send_transaction(transaction)
    print("Transaction response: ", result)