def calculate_risk(summary, threats=None):

    if threats is None:
        threats = []

    score = 0

    # Log Severity
    score += summary["ERROR"] * 3
    score += summary["WARNING"] * 2
    score += summary["INFO"] * 1

    # Threat Severity
    for threat in threats:

        if threat in [
            "Possible Malware Activity",
            "Possible SQL Injection",
            "Credential Dumping",
            "Possible Reverse Shell",
            "Privilege Escalation",
            "Possible Data Exfiltration"
        ]:
            score += 15

        elif threat in [
            "Possible Brute Force Attack",
            "SSH Brute Force",
            "PowerShell Execution Detected",
            "Unauthorized Resource Access",
            "Directory Traversal Attempt",
            "Possible Command Injection"
        ]:
            score += 10

        else:
            score += 5

    # Maximum score
    score = min(score, 100)

    # Risk Level
    if score >= 80:
        risk = "CRITICAL"

    elif score >= 60:
        risk = "HIGH"

    elif score >= 30:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    return {
        "score": score,
        "risk": risk
    }