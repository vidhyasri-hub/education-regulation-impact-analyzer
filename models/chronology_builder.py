import re

chronology_keywords = [
    "in continuation",
    "amended",
    "superseded",
    "revised",
    "modification",
    "previous notification"
]


def build_chronology(text):

    found = []

    lower_text = text.lower()

    for keyword in chronology_keywords:

        if keyword in lower_text:
            found.append(keyword)

    dates = re.findall(
        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',
        text
    )

    references = re.findall(
        r'F\.No\.\s*[\w/-]+',
        text
    )

    return {
        "chronology_signals": found,
        "dates": dates,
        "references": references
    }