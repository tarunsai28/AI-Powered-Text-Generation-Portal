
"""
Workshop 5 - Twitter GPT-2 BPE Tokenization
Prepare train.bin and val.bin for nanoGPT.
"""

import os
import numpy as np
import tiktoken

# Dataset location
data_dir = os.path.dirname(__file__)
input_file = os.path.join(data_dir, "input.txt")

# Read Twitter conversations
with open(input_file, "r", encoding="utf-8") as f:
    data = f.read()

print(f"Total characters: {len(data):,}")

# GPT-2 BPE tokenizer
enc = tiktoken.get_encoding("gpt2")

# Split text into training and validation sets
n = len(data)
train_data = data[:int(n * 0.9)]
val_data = data[int(n * 0.9):]

# Encode text into token IDs
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)

print(f"GPT-2 vocabulary size: {enc.n_vocab:,}")
print(f"Training tokens: {len(train_ids):,}")
print(f"Validation tokens: {len(val_ids):,}")

# Save token IDs
np.array(train_ids, dtype=np.uint16).tofile(
    os.path.join(data_dir, "train.bin")
)

np.array(val_ids, dtype=np.uint16).tofile(
    os.path.join(data_dir, "val.bin")
)

print("BPE dataset preparation completed successfully!")
