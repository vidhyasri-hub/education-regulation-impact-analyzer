import os
import re
from tqdm import tqdm

RAW_FOLDER = "data/raw_text"
CLEAN_FOLDER = "data/cleaned_text"

os.makedirs(CLEAN_FOLDER, exist_ok=True)


def clean_text(text):

    # Remove multiple newlines
    text = re.sub(r"\n+", "\n", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove page numbers
    text = re.sub(r"Page\s+\d+", "", text)

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove unwanted symbols
    text = re.sub(r"[^\w\s.,;:()/%\-]", "", text)

    return text.strip()


def process_cleaning():

    text_files = [
        file for file in os.listdir(RAW_FOLDER)
        if file.endswith(".txt")
    ]

    for text_file in tqdm(text_files):

        path = os.path.join(RAW_FOLDER, text_file)

        with open(path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        cleaned = clean_text(raw_text)

        output_path = os.path.join(
            CLEAN_FOLDER,
            text_file
        )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

    print("Text cleaning completed.")


if __name__ == "__main__":
    process_cleaning()