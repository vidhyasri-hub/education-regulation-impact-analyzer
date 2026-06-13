risk_terms = {

    "high_risk": [
        "mandatory",
        "penalty",
        "strict compliance",
        "revocation"
    ],

    "medium_risk": [
        "recommended",
        "guidelines",
        "subject to approval"
    ],

    "implementation_risk": [
        "infrastructure",
        "funding",
        "resource availability"
    ]
}


def detect_risks(text):

    detected = {}

    lower_text = text.lower()

    for risk_level, keywords in risk_terms.items():

        matches = []

        for keyword in keywords:

            if keyword in lower_text:
                matches.append(keyword)

        if matches:

            detected[risk_level] = matches

    return detected