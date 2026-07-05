def build_threat_severity(threats):

    severity = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    for threat in threats:

        t = threat.lower()

        # Critical Threats
        if any(keyword in t for keyword in [
            "ransomware",
            "malware",
            "remote code execution",
            "privilege escalation"
        ]):
            severity["Critical"] += 1

        # High Threats
        elif any(keyword in t for keyword in [
            "brute force",
            "sql injection",
            "xss",
            "command injection",
            "powershell"
        ]):
            severity["High"] += 1

        # Medium Threats
        elif any(keyword in t for keyword in [
            "failed login",
            "credential",
            "access denied",
            "suspicious"
        ]):
            severity["Medium"] += 1

        # Everything else
        else:
            severity["Low"] += 1

    return severity