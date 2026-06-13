import os
import re
import json
import spacy
from tqdm import tqdm

nlp = spacy.load("en_core_web_sm")

INPUT_FOLDER = "data/cleaned_text"
OUTPUT_FOLDER = "data/structured"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


stakeholder_map = {
    "students": [
        "student",
        "scholarship",
        "admission",
        "learner"
    ],

    "faculty": [
        "faculty",
        "teacher",
        "professor"
    ],

    "institutions": [
        "college",
        "university",
        "institution"
    ],

    "administrators": [
        "administrator",
        "compliance",
        "management"
    ]
}


def detect_stakeholders(text):

    found = []

    lower_text = text.lower()

    for stakeholder, keywords in stakeholder_map.items():

        for keyword in keywords:

            if keyword in lower_text:
                found.append(stakeholder)
                break

    return list(set(found))


def extract_dates(text):

    pattern = r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'

    return re.findall(pattern, text)


def structure_document(text, filename):

    doc = nlp(text)

    sentences = [sent.text.strip() for sent in doc.sents]

    tokens = [
        token.text
        for token in doc
        if not token.is_stop and not token.is_punct
    ]

    lemmas = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct
    ]

    stakeholders = detect_stakeholders(text)

    dates = extract_dates(text)

    structured = {
        "file_name": filename,
        "sentences": sentences,
        "tokens": tokens,
        "lemmas": lemmas,
        "stakeholders": stakeholders,
        "dates": dates,
        "clean_text": text
    }

    return structured


def process_documents():

    files = [
        file for file in os.listdir(INPUT_FOLDER)
        if file.endswith(".txt")
    ]

    for file in tqdm(files):

        path = os.path.join(INPUT_FOLDER, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        structured_data = structure_document(
            text,
            file
        )

        output_file = file.replace(".txt", ".json")

        output_path = os.path.join(
            OUTPUT_FOLDER,
            output_file
        )

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(
                structured_data,
                f,
                indent=4
            )

    print("Structuring completed.")


if __name__ == "__main__":
    process_documents()