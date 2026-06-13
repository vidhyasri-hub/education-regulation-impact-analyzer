# 1. download pdf files and keep it in data folder
# 2. extract text from pdf files and save it in txt files in data folder
# 3. convert Raw PDF Documents to Clean Structured Text + Metadata + NLP Features

#PDF Files ↓ Extract Raw Text ↓ Clean Noise ↓ Split into Sections ↓
#Sentence Segmentation ↓ Tokenization ↓ Stopword Removal ↓ Lemmatization
#↓ Metadata Extraction ↓ Store Structured Output (JSON / CSV / DB)

#| Library | Purpose           |
#| ------- | ----------------- |
#| PyMuPDF | PDF extraction    |
#| spaCy   | NLP preprocessing |
#| pandas  | structured data   |
#| tqdm    | progress bar      |

# Extract Text from PDFs
# Clean Extracted Text
# Structure the Text

#Structured JSON ↓ Topic Classification ↓ Chronology Detection ↓ Impact Analysis ↓ Risk Detection ↓ Gemini Summarization ↓ Dashboard

from models.topic_classfication import classify_document
from models.chronology_builder import build_chronology
from models.impact_analysis import analyze_impact
from models.risk_detection import detect_risks
from models.summarization import summarize_document
from models.report_generation import generate_policy_report

import json

# Load structured JSON
with open(
    "data/structured/sample.json",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)


# Main regulation text
text = data["clean_text"]


# Step 1 — Topic Classification
topic = classify_document(text)


# Step 2 — Chronology Analysis
chronology = build_chronology(text)


# Step 3 — Stakeholder Impact
impact = analyze_impact(text)


# Step 4 — Risk Detection
risk = detect_risks(text)


# Step 5 — Final AI Report
final_report = generate_policy_report(
    document_text=text,
    topic_result=topic,
    chronology_result=chronology,
    impact_result=impact,
    risk_result=risk
)


# Print final report
print(final_report)


#User Uploads PDF ↓ PDF Extraction ↓Preprocessing ↓Topic Classification ↓Chronology Detection ↓Impact Analysis ↓Risk Detection ↓Gemini Policy Intelligence Report ↓Dashboard Visualization


