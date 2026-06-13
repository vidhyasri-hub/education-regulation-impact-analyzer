from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

candidate_labels = [
    "Accreditation",
    "Scholarship",
    "Curriculum",
    "Faculty Policy",
    "Examination",
    "Admissions",
    "Research Policy",
    "Compliance"
]


def classify_document(text):
    result = classifier(
        text[:30000],
        candidate_labels
    )

    return {
        "topic": result["labels"][0],
        "confidence": round(result["scores"][0], 3)
    }


