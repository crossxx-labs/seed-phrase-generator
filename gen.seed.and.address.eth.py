#!/usr/bin/env python3
'''
MIT License

Copyright (c) 2018 Luis Teixeira
Copyright (c) 2019 Niklas Baumstark

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
import sys
from bip_utils import *

seedphrase_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seedphrase')


sys.path.append(seedphrase_module)

from generator import strength, generate_seed
from constants import LANGUAGES, LENGTHS
import argparse
import os

from eth_helper import *


    
if __name__ == '__main__':
    
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
        
        print(mnemonic_to_address(seed))
    except Exception as e:
        print(f"An error occured: {e}")
        exit(1)
