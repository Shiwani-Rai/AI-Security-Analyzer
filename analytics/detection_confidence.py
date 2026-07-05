def build_detection_confidence(threats, risk):

    score = 40

    score += len(threats) * 8

    if risk["risk"] == "HIGH":
        score += 25

    elif risk["risk"] == "MEDIUM":
        score += 15

    else:
        score += 5

    if score > 100:
        score = 100

    return score