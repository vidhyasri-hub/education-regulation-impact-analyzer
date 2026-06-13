import streamlit as st
import tempfile
import json
import os

from preProcessing.textExtraction import extract_text_from_pdf
from preProcessing.textCleaning import clean_text
from preProcessing.textStructuring import structure_document

from models.topic_classfication import classify_document
from models.chronology_builder import build_chronology
from models.impact_analysis import analyze_impact
from models.risk_detection import detect_risks
from models.report_generation import generate_policy_report

from utils.pdfGeneration import create_pdf_report


st.set_page_config(
    page_title="ERIA",
    layout="wide"
)

st.title(
    "Education Regulation Impact Analyzer (ERIA)"
)

st.write(
    "AI-powered education policy intelligence platform"
)


# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.header("Upload Regulation")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

url_input = st.sidebar.text_input(
    "Or Paste Regulation URL"
)


# ======================================================
# MAIN PROCESSING
# ======================================================

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(uploaded_file.read())

        pdf_path = tmp_file.name


    # --------------------------------------------------
    # TEXT EXTRACTION
    # --------------------------------------------------

    raw_text = extract_text_from_pdf(pdf_path)

    cleaned_text = clean_text(raw_text)

    structured_data = structure_document(
        cleaned_text,
        uploaded_file.name
    )


    # --------------------------------------------------
    # AI ANALYSIS
    # --------------------------------------------------

    topic = classify_document(cleaned_text)

    chronology = build_chronology(cleaned_text)

    impact = analyze_impact(cleaned_text)

    risks = detect_risks(cleaned_text)


    # --------------------------------------------------
    # GEMINI REPORT
    # --------------------------------------------------

    with st.spinner("Generating AI policy report..."):

        report = generate_policy_report(
            document_text=cleaned_text,
            topic_result=topic,
            chronology_result=chronology,
            impact_result=impact,
            risk_result=risks
        )


    # ==================================================
    # DASHBOARD OUTPUTS
    # ==================================================

    st.success("Analysis completed.")


    # --------------------------------------------------
    # TOPIC CLASSIFICATION
    # --------------------------------------------------

    st.subheader("Regulation Category")

    st.write(topic)


    # --------------------------------------------------
    # AI SUMMARY PANEL
    # --------------------------------------------------

    st.subheader("AI Policy Intelligence Report")

    st.write(report)


    # --------------------------------------------------
    # STAKEHOLDER IMPACT
    # --------------------------------------------------

    st.subheader("Stakeholder Impact")

    st.json(impact)


    # --------------------------------------------------
    # CHRONOLOGY VIEW
    # --------------------------------------------------

    st.subheader("Policy Chronology")

    st.json(chronology)


    # --------------------------------------------------
    # RISK ANALYSIS
    # --------------------------------------------------

    st.subheader("Risk Detection")

    st.json(risks)


    # --------------------------------------------------
    # DOWNLOAD PDF
    # --------------------------------------------------

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    pdf_path = (
        "outputs/reports/"
        "policy_report.pdf"
    )

    create_pdf_report(
        report,
        pdf_path
    )

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="Download PDF Report",
            data=pdf_file,
            file_name="ERIA_Report.pdf",
            mime="application/pdf"
        )