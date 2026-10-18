
import re
import html
import csv
from pathlib import Path

INPUT_FILE = Path("data/raw/twitter_conversations.txt")
OUTPUT_FILE = Path("data/processed/cleaned_conversations.csv")
SAMPLE_FILE = Path("samples/sample_10.csv")


def clean_text(text):
    # Convert HTML entities: &amp; -> &, &gt; -> >
    text = html.unescape(text)

    # Remove HTML tags such as <b>, </span>, <i>
    text = re.sub(r"</?[a-zA-Z][^>]*>", " ", text)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Remove standalone noise symbols
    text = re.sub(r"(?<!\w)(?:\^\^|[%$@])(?!\w)", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def main():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    SAMPLE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with INPUT_FILE.open("r", encoding="utf-8") as file:
        raw_lines = file.readlines()

    records = []

    for line_number, line in enumerate(raw_lines, start=1):
        original = line.strip()
        cleaned = clean_text(original)

        # Skip empty or noise-only lines
        if not cleaned:
            continue

        records.append({
            "line_number": line_number,
            "original_text": original,
            "cleaned_text": cleaned
        })

    columns = ["line_number", "original_text", "cleaned_text"]

    # Save the full cleaned dataset
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)

    # Save the first 10 records for comparison
    with SAMPLE_FILE.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records[:10])

    print(f"Raw lines: {len(raw_lines)}")
    print(f"Cleaned records: {len(records)}")
    print(f"Removed empty/noise-only lines: {len(raw_lines) - len(records)}")

    print("\n--- First 10 Cleaned Records ---")
    for record in records[:10]:
        print(f"\nOriginal: {record['original_text']}")
        print(f"Cleaned:  {record['cleaned_text']}")

    print(f"\nSaved: {OUTPUT_FILE}")
    print(f"Saved: {SAMPLE_FILE}")


if __name__ == "__main__":
    main()
