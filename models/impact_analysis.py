impact_map = {

    "students": [
        "scholarship",
        "admission",
        "examination"
    ],

    "faculty": [
        "faculty",
        "teacher",
        "research"
    ],

    "institutions": [
        "university",
        "college",
        "institution"
    ],

    "administrators": [
        "compliance",
        "approval",
        "governance"
    ]
}


def analyze_impact(text):

    impacts = {}

    lower_text = text.lower()

    for stakeholder, keywords in impact_map.items():

        matches = []

        for keyword in keywords:

            if keyword in lower_text:
                matches.append(keyword)

        if matches:

            impacts[stakeholder] = {
                "impact_detected": True,
                "keywords": matches
            }

    return impacts