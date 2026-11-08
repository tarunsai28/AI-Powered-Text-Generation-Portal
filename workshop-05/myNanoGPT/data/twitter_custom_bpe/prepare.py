
"""
Workshop 5 - Custom BPE Tokenization
Train a 2,000-token BPE tokenizer on cleaned Twitter text.
Prepare train.bin, val.bin, and tokenizer.json for nanoGPT.
"""

import os
import numpy as np
from tokenizers import Tokenizer, models, trainers, pre_tokenizers, decoders

# --------------------------------------------------
# Dataset paths
# --------------------------------------------------

data_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(data_dir, "input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    data = f.read()

print(f"Total characters: {len(data):,}")

# --------------------------------------------------
# Split dataset: 90% training, 10% validation
# --------------------------------------------------

split_index = int(len(data) * 0.9)

train_text = data[:split_index]
val_text = data[split_index:]

# --------------------------------------------------
# Create custom BPE tokenizer
# --------------------------------------------------

tokenizer = Tokenizer(models.BPE(unk_token="[UNK]"))

# Byte-level tokenization supports emojis and Unicode.
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(
    add_prefix_space=False
)

tokenizer.decoder = decoders.ByteLevel()

trainer = trainers.BpeTrainer(
    vocab_size=2000,
    min_frequency=2,
    special_tokens=["[UNK]"],
    initial_alphabet=pre_tokenizers.ByteLevel.alphabet()
)

# Train only on the training split to avoid data leakage.
tokenizer.train_from_iterator([train_text], trainer=trainer)

# --------------------------------------------------
# Save tokenizer
# --------------------------------------------------

tokenizer_path = os.path.join(data_dir, "tokenizer.json")
tokenizer.save(tokenizer_path)

vocab_size = tokenizer.get_vocab_size()

print(f"Custom BPE vocabulary size: {vocab_size:,}")

# --------------------------------------------------
# Encode training and validation text
# --------------------------------------------------

train_ids = tokenizer.encode(train_text).ids
val_ids = tokenizer.encode(val_text).ids

print(f"Training tokens: {len(train_ids):,}")
print(f"Validation tokens: {len(val_ids):,}")

# --------------------------------------------------
# Save nanoGPT binary datasets
# --------------------------------------------------

np.array(train_ids, dtype=np.uint16).tofile(
    os.path.join(data_dir, "train.bin")
)

np.array(val_ids, dtype=np.uint16).tofile(
    os.path.join(data_dir, "val.bin")
)

print("Custom BPE dataset preparation completed!")
print(f"Tokenizer saved to: {tokenizer_path}")
