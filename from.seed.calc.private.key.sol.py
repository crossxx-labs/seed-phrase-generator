
import sys
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Changes, Bip44Coins

"""
calc private key from seed phrase for sol
Usage: {sys.argv[0]} seed_phrase

reference: 
 - https://github.com/SuperteamDAO/solathon/blob/master/solathon/keypair.py
 - https://github.com/ebellocchia/bip_utils/blob/master/examples/solana_cli.py

"""
import base58
from solathon.keypair import Keypair

# reference: https://stackoverflow.com/questions/66219766/hex-string-to-base58
def hex_to_base58(hex_string):
    if hex_string[:2] in ["0x", "0X"]:
        hex_string = "41" + hex_string[2:]
    bytes_str = bytes.fromhex(hex_string)
    base58_str = base58.b58encode_check(bytes_str)
    return base58_str.decode("UTF-8")


def base58_to_hex(base58_string):
    asc_string = base58.b58decode_check(base58_string)
    return asc_string.hex().upper()

if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        print(f"Usage: {sys.argv[0]} seed_phrase")
        sys.exit(1)
    seed_phrase = sys.argv[1]
    seed_bytes = Bip39SeedGenerator(seed_phrase).Generate("")

    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)

    bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)

    bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

    print(f"Address: {bip44_chg_ctx.PublicKey().ToAddress()}")
    private_key = hex_to_base58(bip44_chg_ctx.PrivateKey().Raw().ToHex())
    print(f"Private key: {private_key}")
    kp = Keypair.from_private_key(private_key)
    print(f"Phantom private key: {kp.private_key}")
    
