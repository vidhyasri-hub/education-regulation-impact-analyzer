import os
import fitz  # PyMuPDF
from tqdm import tqdm

PDF_FOLDER = "data/pdfs"
OUTPUT_FOLDER = "data/raw_text"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    full_text = ""

    for page in doc:
        text = page.get_text()
        full_text += text

    return full_text


def process_pdfs():

    pdf_files = [
        file for file in os.listdir(PDF_FOLDER)
        if file.endswith(".pdf")
    ]

    for pdf_file in tqdm(pdf_files):

        pdf_path = os.path.join(PDF_FOLDER, pdf_file)

        extracted_text = extract_text_from_pdf(pdf_path)

        output_file = pdf_file.replace(".pdf", ".txt")

        output_path = os.path.join(
            OUTPUT_FOLDER,
            output_file
        )

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(extracted_text)

    print("PDF extraction completed.")


if __name__ == "__main__":
    process_pdfs()