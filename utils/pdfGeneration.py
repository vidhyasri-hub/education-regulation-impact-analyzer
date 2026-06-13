from fpdf import FPDF


def clean_pdf_text(text):

    replacements = {
        "–": "-",
        "—": "-",
        "‘": "'",
        "’": "'",
        "“": '"',
        "”": '"',
        "•": "-",
        "\u00a0": " "
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    return text

def sanitize_text(text):
    # Convert unsupported Unicode characters
    # into safe latin-1 compatible text
        return (
            text
            .encode("latin-1", "replace")
            .decode("latin-1")
     )


def create_pdf_report(report_text, output_path):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    # CLEAN UNICODE CHARACTERS
    report_text = clean_pdf_text(report_text)

    # SANITIZE TEXT
    report_text = sanitize_text(report_text)

    lines = report_text.split("\n")

    for line in lines:

        pdf.multi_cell(0, 10, line)

    pdf.output(output_path)