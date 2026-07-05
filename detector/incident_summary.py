def generate_summary(summary, risk):

    findings = []

    if summary["ERROR"] > 0:
        findings.append(
            f"Detected {summary['ERROR']} ERROR events."
        )

    if summary["WARNING"] > 0:
        findings.append(
            f"Detected {summary['WARNING']} WARNING events."
        )

    if risk["risk"] == "HIGH":
        threat = (
            "Potential security incident requiring immediate investigation."
        )

    elif risk["risk"] == "MEDIUM":
        threat = (
            "Suspicious activity detected. Review recommended."
        )

    else:
        threat = (
            "No significant threats identified."
        )

    recommendations = [
        "Review system logs.",
        "Investigate repeated errors.",
        "Check authentication activity.",
        "Verify system availability."
    ]

    return {
        "findings": findings,
        "threat": threat,
        "recommendations": recommendations
    }