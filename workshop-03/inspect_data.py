
from pathlib import Path

# Location of the raw dataset
file_path = Path("data/raw/twitter_conversations.txt")

# Read the dataset
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Basic dataset statistics
print("Total lines:", len(lines))
print("Non-empty lines:", sum(bool(line.strip()) for line in lines))
print("Empty lines:", sum(not line.strip() for line in lines))

# Preview the first 10 lines
print("\n--- First 10 Lines ---")
for index, line in enumerate(lines[:10], start=1):
    print(f"{index}: {line.strip()}")
