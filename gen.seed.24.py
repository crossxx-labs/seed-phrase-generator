import sys
import os

seedphrase_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seedphrase')
sys.path.append(seedphrase_module)

from generator import strength, generate_seed


num_words = 24
strength = strength(num_words)

seed = generate_seed(strength, 'en')
print(seed)