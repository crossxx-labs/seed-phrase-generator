import os
import sys
from bip_utils import *

seedphrase_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seedphrase')


sys.path.append(seedphrase_module)

from generator import strength, generate_seed
from constants import LANGUAGES, LENGTHS
import argparse
import os


parser = argparse.ArgumentParser(
    description="Generate a seed phrase of variable length.")

parser.add_argument("length", type=int, choices=LENGTHS, metavar="length",
                    help="Length of seed phrase to be generated. The possible lengths are 12, 15, 18, 21 or 24 words.")
# parser.add_argument("-s", "--save", action="store_true",
#                     help="Save the seed phrase in a file 'seed.txt'.")
parser.add_argument("-l", "--language", choices=LANGUAGES.keys(), metavar="language",
                    help=f"The language in witch to generate the seed phrase. The possible languages are: en (english), zh (chinese simplified), zh2 (chinese traditional), fr (french), it (italian), ja (japanese), ko (korean), es (spanish). The default language is en (english)", default="en")

args = parser.parse_args()

try:
    strength = strength(args.length)

    seed = generate_seed(strength, args.language)
    print(seed)
    
    MNEMONIC = seed

    seed_bytes = Bip39SeedGenerator(MNEMONIC).Generate("")

    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)

    bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)

    bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

    print(bip44_chg_ctx.PublicKey().ToAddress())
except Exception as e:
    print(f"An error occured: {e}")
    exit(1)